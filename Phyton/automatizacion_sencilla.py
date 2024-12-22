from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Ruta y función para el servicio GET
@app.route('/users', methods=['GET'])
def get_users():
    # URL de la API externa
    api_url = 'https://jsonplaceholder.typicode.com/users'
    
    # Hacer la solicitud GET a la API externa
    response = requests.get(api_url)
    
    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener los datos en formato JSON
        data = response.json()
        
        # Retornar los datos en una lista
        return jsonify(data)
    else:
        # Retornar un mensaje de error si la solicitud falla
        return jsonify({'error': 'No se pudieron obtener los datos'}), 500

if __name__ == '__main__':
    app.run(debug=True)
