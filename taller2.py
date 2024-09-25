import csv
import json


# Cargar los datos desde los archivos CSV
with open('data/categorias.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    categorias = list(reader)

with open('data/productos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    productos = list(reader)

# Crear un diccionario para almacenar las categorías y sus productos
categorias_dict = {}

# Organizar los productos bajo sus respectivas categorías
for categoria in categorias:
    categoria_id = int(categoria['id'])
    categorias_dict[categoria_id] = {
        "id": categoria_id,
        "modelo": categoria['modelo'],
        "productos": []
    }

for producto in productos:
    categoria_id = int(producto['id_categoria'])
    producto_info = {
        "marca": producto['marca'],
        "precio": float(producto['precio']),
        "unidades_disponibles": int(producto['unidades_disponibles'])
    }
    categorias_dict[categoria_id]['productos'].append(producto_info)

# Convertir el diccionario a una lista
categorias_list = list(categorias_dict.values())

# Crear el esquema JSON final
esquema_json = {
    "categorias": categorias_list
}

# Convertir a JSON
esquema_json_str = json.dumps(esquema_json, indent=4, ensure_ascii=False)

# Mostrar el JSON resultante
print(esquema_json_str)

# También puedes guardarlo en un archivo JSON si lo deseas
with open('esquema.json', 'w', encoding='utf-8') as json_file:
    json_file.write(esquema_json_str)

