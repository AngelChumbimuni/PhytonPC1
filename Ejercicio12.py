
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}


nombre_archivo = input("Ingrese el nombre del archivo: ")


if '.' in nombre_archivo:
    extension = nombre_archivo.split('.')[-1].lower()

    # Verificar la extensión y mostrar el tipo MIME correspondiente
    tipo_mime = tipos_mime.get(extension, 'application/octet-stream')
    print(f"El tipo MIME del archivo {nombre_archivo} es: {tipo_mime}")
else:
    print("El nombre del archivo no tiene una extensión reconocible.")