dict_convert_meter = { "km": "1000",
                      "hm": "100",
                      "dam": "10",
                      "milla": "1609.344"

}

print("Convierte tus medidas a metros!")
medida_ingr= float(input("Ingrese el valor de la medida \n"))
print("Que unidad de medida es la que ha ingresado?")
unidad_ingr= str(input("km \nhm\ndam\nmilla\n")).lower()

if unidad_ingr in dict_convert_meter:
        unidad_conver= float(dict_convert_meter[unidad_ingr])*medida_ingr
        print(medida_ingr,unidad_ingr,"a metros es: ",unidad_conver,"m")
else:
        print("La unidad de medida ingresada no se encuentra en la lista de opciones")