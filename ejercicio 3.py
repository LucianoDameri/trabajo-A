import os
import time
nombres=[]
os.system('cls')
while True:
    nombre=input("Ingrese nombre: ")
    nombres.append(nombre)
    opt=input("¿quieres seguir agregando nombre? (si o no): ").lower()
    if opt in ("no","No","nO","NO"):
        break

posi = 0
for x in range(len(nombres)):
        if x==0:
            nombre_masc=nombres[0]
        else:
            if len(nombres[x])<len(nombre_masc):
                nombre_masc=nombres[x]
                posi = x

nombre_masc= nombres.pop(posi)
print(f"El nombre con la menor cantidad de caracteres es ('{nombre_masc}') ")
os.system('cls')
print('.')
os.system('cls')
time.sleep(4)
print('..')
os.system('cls')
time.sleep(4) 
print('...')
os.system('cls')
time.sleep(4)
print('se elimino correctamente')

