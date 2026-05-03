"""
API Web - IA-Mixita
Ejecutar con: python app.py
Acceder en: http://localhost:5000
"""

from flask import Flask, render_template, jsonify, request
import sys
import os

# Agregar el directorio padre al path para importar ia_mixita
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ia_mixita import IAMixita

app = Flask(__name__)
mixita = IAMixita()


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@app.route('/api/info')
def get_info():
    """Obtiene información de la IA"""
    return jsonify(mixita.get_info())


@app.route('/api/specialties')
def get_specialties():
    """Obtiene lista de especialidades"""
    return jsonify({
        "specialties": mixita.get_specialties()
    })


@app.route('/api/deploy', methods=['POST'])
def deploy_module():
    """Despliega un módulo específico"""
    data = request.json
    module_name = data.get('module_name', 'Unknown Module')
    result = mixita.deploy_module(module_name)
    return jsonify({
        "success": True,
        "message": result
    })


@app.route('/api/solve', methods=['POST'])
def solve_system():
    """Resuelve un sistema complejo"""
    data = request.json
    context = data.get('context', 'General System')
    result = mixita.solve_complex_system(context)
    return jsonify({
        "success": True,
        "result": result
    })


@app.route('/api/status')
def get_status():
    """Obtiene estado actual"""
    return jsonify({
        "name": mixita.name,
        "status": mixita.status,
        "online": True
    })


if __name__ == '__main__':
    print("="*60)
    print("🚀 IA-Mixita - API Web")
    print("="*60)
    print("Accede a: http://localhost:5000")
    print("API disponible en: http://localhost:5000/api/")
    print("="*60)
    app.run(debug=True, host='0.0.0.0', port=5000)
