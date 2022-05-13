estudiante1 = {
    "cédula": "00014301503",
    "nombre": "Pepito",
    "nota_fundamento": 4.3  
}

estudiante2 = {
    "cédula": "1037678471",
    "nombre": "Fulanito",
    "nota_fundamento": 3.2  
}

estudiante3 = {
    "cédula": "1037678471",
    "nombre": "Fulanito",
    "nota_fundamento": 5  
}

grupo = [estudiante1, estudiante2, estudiante3]

print (estudiante1["nota_fundamento"])

print(grupo[1]["nota_fundamento"])

notas= []
for estudiante in grupo:
    notas.append(estudiante["nota_fundamento"])

print(notas)  
promedio=sum(notas)/len(grupo)
print(promedio)


def ordenamiento_burbuja(lista):
    n = len (lista) ## trabajando por len
    
    for i in range(n): 
        print('este es i', i)
        for j in range(0, n - i - 1) : #el -1 es por indices 0
            print('este es j ', j)
            print(lista)
            if lista[j]["nota_fundamento"] < lista[j + 1]["nota_fundamento"]:
                lista[j], lista[j+1] = lista[j+1], lista[j] ##intercambiamos los elementos

    return lista

grupo_honor= ordenamiento_burbuja(grupo)
print("grupo",grupo_honor)