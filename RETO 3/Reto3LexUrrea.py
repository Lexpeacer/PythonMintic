def quitar_repetidos(dato):
    nuevo_caracter = ""
    caracter_anterior = ""
    for caracter in dato:
        if len(nuevo_caracter) == 0:
            nuevo_caracter += caracter
            caracter_anterior = caracter
        if caracter == caracter_anterior:
            continue
        else:
            nuevo_caracter += caracter
            caracter_anterior = caracter
    return nuevo_caracter

tupla = input()
tupla=tupla.upper()
tupla=tupla.replace(",","")

paquetes=[]
contador=[0]
paquetes.append(tupla[0])

for caracter in tupla:
        if caracter != paquetes[-1]:
          paquetes.append(caracter)
          contador.append(1)
        else:
          contador[-1]+=1

print(*contador)
print(' '.join(quitar_repetidos(tupla)))