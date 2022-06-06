import subprocess
import re

try:
    #Ejecutar el comando who -H y guardar el output formateado en un csv
    raw_output = subprocess.check_output("who -H | awk '{print $1, $5}'", shell=True) #El retorno se guarda en forma de bytes
    output = raw_output.decode('utf-8') #Se transforma a str
    
    #Formatear el output
    lista_output = output.split('\n') #Separa el output
    lista_output.pop(-1) #Elimina el ultimo elemento que queda rebundante
    for i, j in enumerate(lista_output): #Separar en comas por palabras
        lista_output[i] = re.sub('\s+' , ',', j.strip())
    
    #Remobrar los headers
    lista_output[0] = "USER, IP"

    #Escribir en un archivo csv
    with open ('./resultados/verificacion_usuarios.csv', 'w') as archivo_csv:
        for i in lista_output:
            archivo_csv.write (i + '\n')


except Exception:
    print("Error al mostrar los usuarios conectados")