"""
CLI Interactiva - IA-Mixita
Ejecutar con: python app.py
"""

import sys
import os
from datetime import datetime

# Agregar el directorio padre al path para importar ia_mixita
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ia_mixita import IAMixita


class IAMixitaCLI:
    def __init__(self):
        self.mixita = IAMixita()
        self.running = True
        self.history = []
    
    def print_header(self):
        """Imprime el encabezado de la aplicación"""
        print("\n" + "=" * 70)
        print("🤖  IA-MIXITA - Sistema Inteligente Avanzado Multinivel")
        print("=" * 70)
        print(f"Estado: {self.mixita.status}")
        print(f"Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70 + "\n")
    
    def print_menu(self):
        """Imprime el menú principal"""
        print("\n📋 MENÚ PRINCIPAL")
        print("-" * 70)
        print("1. 📌 Ver Información de la IA")
        print("2. 🎯 Ver Especialidades")
        print("3. 🚀 Desplegar Módulo Específico")
        print("4. ⚙️  Resolver Sistema Complejo")
        print("5. 📊 Ver Historial de Operaciones")
        print("6. ❌ Salir")
        print("-" * 70)
    
    def show_info(self):
        """Muestra información de la IA"""
        info = self.mixita.get_info()
        print("\n" + "=" * 70)
        print("📌 INFORMACIÓN DE IA-MIXITA")
        print("=" * 70)
        print(f"Nombre: {info['nombre']}")
        print(f"Rol: {info['rol']}")
        print(f"Estado: {info['estado']}")
        print("=" * 70)
    
    def show_specialties(self):
        """Muestra las especialidades"""
        specialties = self.mixita.get_specialties()
        print("\n" + "=" * 70)
        print("🎯 ESPECIALIDADES")
        print("=" * 70)
        for i, spec in enumerate(specialties, 1):
            print(f"{i}. {spec}")
        print("=" * 70)
    
    def deploy_module(self):
        """Despliega un módulo"""
        print("\n" + "=" * 70)
        print("🚀 DESPLEGAR MÓDULO")
        print("=" * 70)
        print("\nMódulos disponibles:")
        modules = [
            "Blockchain & Tokens",
            "Monitoreo de Ecosistemas",
            "Infraestructura de Redes",
            "Algoritmos Avanzados",
            "Otro (Personalizado)"
        ]
        
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module}")
        
        try:
            choice = input("\nSelecciona un módulo (1-5) o ingresa nombre: ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= 5:
                if int(choice) == 5:
                    module_name = input("Nombre del módulo personalizado: ").strip()
                else:
                    module_name = modules[int(choice) - 1]
            else:
                module_name = choice
            
            if module_name:
                result = self.mixita.deploy_module(module_name)
                print(f"\n✓ {result}")
                self.history.append(f"Deploy: {module_name}")
            else:
                print("❌ Error: Nombre de módulo vacío")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def solve_system(self):
        """Resuelve un sistema complejo"""
        print("\n" + "=" * 70)
        print("⚙️  RESOLVER SISTEMA COMPLEJO")
        print("=" * 70)
        print("\nContextos de ejemplo:")
        contexts = [
            "Red de Antenas y Servidores",
            "Sistemas de Blockchain",
            "Monitoreo Ambiental Integral",
            "Red Global de IoT",
            "Otro (Personalizado)"
        ]
        
        for i, ctx in enumerate(contexts, 1):
            print(f"{i}. {ctx}")
        
        try:
            choice = input("\nSelecciona un contexto (1-5) o ingresa uno personalizado: ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= 5:
                if int(choice) == 5:
                    context = input("Describe el contexto: ").strip()
                else:
                    context = contexts[int(choice) - 1]
            else:
                context = choice
            
            if context:
                print("\n⏳ Analizando arquitectura...")
                result = self.mixita.solve_complex_system(context)
                print(f"\n✓ {result}")
                self.history.append(f"Solve: {context}")
            else:
                print("❌ Error: Contexto vacío")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def show_history(self):
        """Muestra el historial de operaciones"""
        print("\n" + "=" * 70)
        print("📊 HISTORIAL DE OPERACIONES")
        print("=" * 70)
        
        if not self.history:
            print("No hay operaciones registradas aún.")
        else:
            for i, operation in enumerate(self.history, 1):
                print(f"{i}. {operation}")
        
        print("=" * 70)
    
    def run(self):
        """Ejecuta la aplicación CLI"""
        self.print_header()
        
        while self.running:
            self.print_menu()
            choice = input("\nSelecciona una opción (1-6): ").strip()
            
            if choice == "1":
                self.show_info()
            elif choice == "2":
                self.show_specialties()
            elif choice == "3":
                self.deploy_module()
            elif choice == "4":
                self.solve_system()
            elif choice == "5":
                self.show_history()
            elif choice == "6":
                print("\n👋 ¡Hasta luego!")
                self.running = False
            else:
                print("\n❌ Opción inválida. Por favor, intenta de nuevo.")
        
        print("\n" + "=" * 70)
        print("Aplicación finalizada.")
        print("=" * 70 + "\n")


if __name__ == '__main__':
    try:
        cli = IAMixitaCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación interrumpida por el usuario.")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
