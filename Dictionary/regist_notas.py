num_estudia = int(input("Ingrese el numero de estudiantes que se van a registrar: "))
num_notas = int(input("Ingrese la cantidad de notas que va ingresar por estudiante: "))
contador_estu =1
dict_estudiante = {}
promedio_general = 0
sumaPromedios=0
while(contador_estu <= num_estudia):
    print("Estudiante N. ",contador_estu)
    contador_notas =1
    sum_notas=0
    while(contador_notas <= num_notas):
        print("Ingrese la nota ", contador_notas)
        notas_estu= float(input())
        sum_notas+=notas_estu
        contador_notas+=1
    promedio= sum_notas/num_notas
    sumaPromedios+= promedio 
    dict_estudiante["Estudiante",contador_estu]= promedio
    print("El promedio del estudiante N", contador_estu, "es: ", promedio)
    contador_estu+=1
    promedio_general= sumaPromedios/num_estudia
    
dict_estudiante["Promedio General"]= promedio_general
print("\nEl promedio general es: ",promedio_general)
print(dict_estudiante)

