#Empresa importadora de productos
print("Bienvenido\nPor favor, señor usuario, ingrese los siguientes datos:\nPais de origen\nValor de la mercancia\nPeso total de la mercancia")

pais = str(input("Pais: "))
valor = float(input("Valor: "))
peso = float(input("Peso: "))
 
#Definimos continente aca 
def continente(pais, peso):
    if pais == "Argentina" or pais == "Colombia":
        s = 4 * peso
        return "Sudamerica", s
    elif pais == "Belgica" or pais == "Italia":
        e = 7 * peso
        return "Europa", e
    elif pais == "India" or pais == "Tailandia":
        a = 9 * peso
        return  "Asia", a
    else:
        return "Lo lamento. No realizamos envios a tu pais :(", 0

#Definimos la condicional para el tipo de importacion
def importacion(valor):
    if valor < 5000:
        c = "Importacion pequeña"
        return c
    elif 5000 <= valor <= 15000:
        i = "Importacion mediana"
        return i
    else:
        o = "Importacion grande"
        return o    

#simplificacion de las funciones
ncontinente, costo_trans = continente(pais, peso)
rimportacion = importacion(valor)
#Factura
print("Contiente: ", ncontinente, "\nTransporte: ", costo_trans, "USD", "\ntipo: ", rimportacion)