import requests

# URL de la API
url = 'https://jsonplaceholder.typicode.com/users/1'  # ID de usuario 1

# Realizamos la solicitud GET
response = requests.get(url)

# Comprobamos si la respuesta fue exitosa
if response.status_code == 200:
    # Convertimos la respuesta a formato JSON
    user_data = response.json()
    
    # Extraemos los campos que nos interesan
    name = user_data['name']
    email = user_data['email']
    address = user_data['address']
    street = address['street']
    city = address['city']
    
    # Mostramos los datos
    print(f"Nombre: {name}")
    print(f"Correo electrónico: {email}")
    print(f"Dirección: {street}, {city}")
else:
    print(f"Error en la solicitud: {response.status_code}")
