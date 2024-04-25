 # Se indica lo necesario para hacer las arepas
print("Para hacer arepas, necesitara los siguientes ingredientes: Harina, Agua, Aceite y Sal. Tambien necesitara un Bol y un Budare.")


# Se piden los ingredientes al usuario
harina_main = input("Ingrese la cantidad de harina en tazas: ")
agua_main = input("Ingrese la cantidad de agua en tazas: ")
sal_main = input("Ingrese la cantidad de sal en cucharaditas: ")

# Se convierten los valores a int y float
harina = int(harina_main)
agua = int(agua_main)
sal = float(sal_main)

# Se calcula la masa de arepas resultante
bol = harina + agua + sal * (1/16/3)

# Se muestra el resultado correspondiente al usuario
print("La cantidad de masa de las arepas resultante es:", bol)

# Se indica los pasos posteriores (no es requerido para la actividad)
print("Al tener esta masa lista, proceda a amasarla hasta que quede uniforme.")
print("Luego, aplastela en forma de disco y ponga a calentar el budare con aceite.")
print("Una vez el budare este caliente, ponga su arepa y deje que se cocine a fuego medio por 10 minutos cada cara.")