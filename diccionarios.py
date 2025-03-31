# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Ana García",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor para la "profesion" (esto ya estaba en la creación, pero se puede modificar)
informacion_personal["profesion"] = "Desarrolladora Web"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
