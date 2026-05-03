"""
App de Escritorio - IA-Mixita con PyQt6
Ejecutar con: python app.py
"""

import sys
import os
import json

# Agregar el directorio padre al path para importar ia_mixita
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QLineEdit, QTabWidget, QScrollArea
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QColor
from ia_mixita import IAMixita


class WorkerThread(QThread):
    """Thread para ejecutar operaciones sin bloquear la UI"""
    result_ready = pyqtSignal(str)
    
    def __init__(self, operation, *args):
        super().__init__()
        self.operation = operation
        self.args = args
        self.mixita = IAMixita()
    
    def run(self):
        try:
            if self.operation == "deploy":
                result = self.mixita.deploy_module(self.args[0])
            elif self.operation == "solve":
                result = self.mixita.solve_complex_system(self.args[0])
            else:
                result = "Operación desconocida"
            self.result_ready.emit(result)
        except Exception as e:
            self.result_ready.emit(f"Error: {str(e)}")


class IAMixitaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mixita = IAMixita()
        self.init_ui()
        self.worker = None
    
    def init_ui(self):
        """Inicializa la interfaz de usuario"""
        self.setWindowTitle("IA-Mixita - Aplicación de Escritorio")
        self.setGeometry(100, 100, 1000, 700)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        
        # Título
        title = QLabel("🤖 IA-Mixita - Sistema Inteligente Avanzado")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # Tabs
        tabs = QTabWidget()
        main_layout.addWidget(tabs)
        
        # Tab 1: Información
        info_tab = self.create_info_tab()
        tabs.addTab(info_tab, "Información")
        
        # Tab 2: Módulos
        modules_tab = self.create_modules_tab()
        tabs.addTab(modules_tab, "Desplegar Módulos")
        
        # Tab 3: Sistema
        system_tab = self.create_system_tab()
        tabs.addTab(system_tab, "Resolver Sistema")
        
        self.setStyleSheet(self.get_stylesheet())
    
    def create_info_tab(self):
        """Crea la pestaña de información"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        info = self.mixita.get_info()
        
        # Información formateada
        info_text = f"""
        📌 NOMBRE: {info['nombre']}
        
        👤 ROL: {info['rol']}
        
        ⚡ ESTADO: {info['estado']}
        
        🎯 ESPECIALIDADES:
        """
        
        for spec in info['especialidades']:
            info_text += f"\n        • {spec}"
        
        text_display = QTextEdit()
        text_display.setText(info_text)
        text_display.setReadOnly(True)
        text_display.setFont(QFont("Courier", 10))
        layout.addWidget(text_display)
        
        return widget
    
    def create_modules_tab(self):
        """Crea la pestaña de módulos"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Instrucción
        label = QLabel("Ingresa el nombre del módulo a desplegar:")
        layout.addWidget(label)
        
        # Input
        self.module_input = QLineEdit()
        self.module_input.setPlaceholderText("Ej: Blockchain & Tokens")
        self.module_input.returnPressed.connect(self.deploy_module)
        layout.addWidget(self.module_input)
        
        # Botón
        deploy_btn = QPushButton("🚀 Desplegar Módulo")
        deploy_btn.clicked.connect(self.deploy_module)
        deploy_btn.setMinimumHeight(40)
        layout.addWidget(deploy_btn)
        
        # Output
        layout.addWidget(QLabel("Resultado:"))
        self.module_output = QTextEdit()
        self.module_output.setReadOnly(True)
        self.module_output.setFont(QFont("Courier", 10))
        layout.addWidget(self.module_output)
        
        return widget
    
    def create_system_tab(self):
        """Crea la pestaña de sistema"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Instrucción
        label = QLabel("Describe el contexto del sistema a resolver:")
        layout.addWidget(label)
        
        # Input
        self.context_input = QTextEdit()
        self.context_input.setPlaceholderText("Describe el contexto...")
        self.context_input.setMaximumHeight(100)
        layout.addWidget(self.context_input)
        
        # Botón
        solve_btn = QPushButton("⚙️ Ejecutar Protocolo de Optimización")
        solve_btn.clicked.connect(self.solve_system)
        solve_btn.setMinimumHeight(40)
        layout.addWidget(solve_btn)
        
        # Output
        layout.addWidget(QLabel("Resultado:"))
        self.system_output = QTextEdit()
        self.system_output.setReadOnly(True)
        self.system_output.setFont(QFont("Courier", 10))
        layout.addWidget(self.system_output)
        
        return widget
    
    def deploy_module(self):
        """Despliega un módulo"""
        module_name = self.module_input.text().strip()
        if not module_name:
            self.module_output.setText("Error: Por favor ingresa un nombre de módulo")
            return
        
        self.module_output.setText("⏳ Procesando...")
        self.worker = WorkerThread("deploy", module_name)
        self.worker.result_ready.connect(self.on_deploy_complete)
        self.worker.start()
    
    def on_deploy_complete(self, result):
        """Se ejecuta cuando el deploy termina"""
        self.module_output.setText(f"✓ {result}")
    
    def solve_system(self):
        """Resuelve un sistema complejo"""
        context = self.context_input.toPlainText().strip()
        if not context:
            self.system_output.setText("Error: Por favor describe el contexto del sistema")
            return
        
        self.system_output.setText("⏳ Analizando sistema...")
        self.worker = WorkerThread("solve", context)
        self.worker.result_ready.connect(self.on_solve_complete)
        self.worker.start()
    
    def on_solve_complete(self, result):
        """Se ejecuta cuando el solve termina"""
        self.system_output.setText(f"✓ {result}")
    
    @staticmethod
    def get_stylesheet():
        """Returns custom stylesheet"""
        return """
        QMainWindow {
            background-color: #f5f5f5;
        }
        QLabel {
            color: #333;
        }
        QLineEdit, QTextEdit {
            background-color: white;
            border: 2px solid #ddd;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            color: #333;
        }
        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #667eea;
        }
        QPushButton {
            background-color: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-weight: bold;
            font-size: 12px;
        }
        QPushButton:hover {
            background-color: #764ba2;
        }
        QPushButton:pressed {
            background-color: #5568d3;
        }
        QTabWidget::pane {
            border: 1px solid #ddd;
        }
        QTabBar::tab {
            background-color: #e0e0e0;
            padding: 8px 20px;
            margin: 2px;
        }
        QTabBar::tab:selected {
            background-color: #667eea;
            color: white;
        }
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IAMixitaApp()
    window.show()
    sys.exit(app.exec())
