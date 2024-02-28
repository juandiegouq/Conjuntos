
from matplotlib_venn import venn3
from matplotlib import pyplot as plt




# Intersección: Este método encuentra la interección entre dos conjuntos. Se hace esto revisando los elementos que se encuentran en común
def inter(c1, c2):
    cr = []
    for i in c1:
        for j in c2:
            if i == j:
                cr.append(i)
    return cr


# Resta: este método encuentra la intersección entre dos conjuntos. Se toman todos los datos menos la intersección
def resta(c1, c2):
    cr = c1.copy()
    intersecc = inter(c1, c2)
    for i in intersecc:
        cr.remove(i)
    return cr


# Union: este método retorna la union de dos conjuntos, c1 y c2, sumando las restas y la intersección
def union(c1, c2):
    cr = resta(c1, c2) + resta(c2, c1) + inter(c1, c2)
    return cr


# Complemtento: este método encuentra el complemento. Se requiere el conjunto, el universal y se restan
def compl(c, u):
    cr = resta(u, c)
    return cr


# Cardinalidad: este método encuentra la cardinalidad de un conjunto, usa la función de longitud
def card(c):
    return len(c)


# Subconjunto: este método encuentra si un conjunto c1 es subconjunto de un conjunto c2, se sabe si la longitud del conjunto restante es 0, retorna true o false
def subcj(c1, c2):
    r = False
    rest = resta(c1, c2)
    if len(rest) == 0:
        r = True
    return r


# Disjuntos
def disj(c1, c2):
    r = False
    intersecc = inter(c1, c2)
    if len(intersecc) == 0:
        r = True
    return r

# Crea un conjunto con los datos que da el usuario

def crearConjunto():
    cr = []
    i = int(input("Número de elementos del conjunto"))
    for k in range(i):
        a = input("Número")
        cr.append(a)
    return cr

#metodo para limpiar consola
def limpiar_consola():
    print('\n' * 100)


#metodo para mostrar menu valores

def mostrar_menu_valores():
    print("1. Usar valores por defecto:\n a = {1,3,5,7}\n b = {2,4,6,8}\n c = {1,2,3,4,5,6,7}\n"
         "2. Usar valores personalizados \n")



#metodo para mostrar menu operaciones
def mostrar_menu_operaciones():
    print("1. Union \n"
          "2. Interseccion \n"
          "3. Resta \n"
          "4. Complemento \n"
          "5. Cardinalidad \n"
          "6. Subconjunto \n"
          "7. Disjunto \n"
          "8. Graficar \n"
          "9. Salir \n")



#método para imprimir un conjunto
def imprimirConjunto(conjunto):
    for e in conjunto:
        print(e)





#funcion que grafica el diagrama de venn con 3 conjuntos
def graficar_venn(a, b, c):
    # Obtener longitudes de conjuntos y calcular intersecciones
    len_a, len_b, len_c = len(a), len(b), len(c)
    interseccion_ab = len(inter(a,b))
    interseccion_ac = len(inter(a,c))
    interseccion_bc = len(inter(b,c))
    interseccion_abc = len(inter(inter(a,c),b))

    # Calcular las longitudes de los subconjuntos para el diagrama de Venn
    solo_a = len_a - interseccion_ab - interseccion_ac + interseccion_abc
    solo_b = len_b - interseccion_ab - interseccion_bc + interseccion_abc
    solo_c = len_c - interseccion_ac - interseccion_bc + interseccion_abc
    inter_ab = interseccion_ab - interseccion_abc
    inter_ac = interseccion_ac - interseccion_abc
    inter_bc = interseccion_bc - interseccion_abc

    # Crear el diagrama de Venn
    venn_diagram = venn3(subsets=(solo_a, solo_b, inter_ab, solo_c, inter_ac, inter_bc, interseccion_abc))

    # Asignar etiquetas de los conjuntos
    if venn_diagram.get_label_by_id('100') is not None:
        venn_diagram.get_label_by_id('100').set_text('\n'.join(map(str, resta(resta(a,b),c))))
    if venn_diagram.get_label_by_id('010') is not None:
        venn_diagram.get_label_by_id('010').set_text('\n'.join(map(str, resta(resta(b,a),c))))
    if venn_diagram.get_label_by_id('110') is not None:
        venn_diagram.get_label_by_id('110').set_text('\n'.join(map(str, resta(inter(a,b),c))))
    if venn_diagram.get_label_by_id('001') is not None:
        venn_diagram.get_label_by_id('001').set_text('\n'.join(map(str, resta(resta(c,a),b))))
    if venn_diagram.get_label_by_id('101') is not None:
        venn_diagram.get_label_by_id('101').set_text('\n'.join(map(str, resta(inter(a,c),b))))
    if venn_diagram.get_label_by_id('011') is not None:
        venn_diagram.get_label_by_id('011').set_text('\n'.join(map(str, resta(inter(b,c),a))))
    if venn_diagram.get_label_by_id('111') is not None:
        venn_diagram.get_label_by_id('111').set_text('\n'.join(map(str, inter(inter(a,b),c))))

    # Mostrar el diagrama de Venn
    plt.title("Diagrama de Venn de 3 conjuntos")
    plt.show()
    


#funcion principal del programa, muestra menus y hace la lógica
def main():
    #se muestra la opción de ingresar valores por defecto o usar valores personalizados y se valida que elija opción correcta
    while True:
        mostrar_menu_valores()
        opcion = input("Selecciona una opcion \n")
        if opcion == "1" or opcion == "2":
            break
        else:
            print("Opcion invalida \n")

    #si se eligen valores por defecto
    if opcion == "1":
        limpiar_consola()
        a = [1, 3, 5, 7]
        b = [2, 4, 6, 8]
        c = [1, 2, 3, 4, 5, 6, 7]
        u = [1, 2, 3, 4, 5, 6, 7, 8]
        vacio = []
    #si se eligen valores personalizados
    else:
        limpiar_consola()
        print("Ingrese el conjunto a \n")
        a = crearConjunto()
        print("Ingrese el conjunto b \n")
        b = crearConjunto()
        print("Ingrese el conjunto c \n")
        c = crearConjunto()
        print("Ingrese el conjunto universal \n")
        u = crearConjunto()
        vacio = []
        limpiar_consola()

    #ciclo del menú de operaciones entre conjuntos
    while True:
        mostrar_menu_operaciones()
        opcion = input("Selecciona una opcion \n")
        if opcion == "1":
            union1 = union(a,b)
            union2 = union(a,c)
            union3 = union(b,c)
            print("A u B = \n", union1)
            print("A u C = \n", union2)
            print("B u C = \n", union3)
        elif opcion == "2":
            intersec1 = inter(a,b)
            intersec2 = inter(a,c)
            intersec3 = inter(b,c)
            print("A n B = \n", intersec1)
            print("A n C = \n", intersec2)
            print("B n C = \n", intersec3)
        elif opcion == "3":
            resta1 = resta(a,b)
            resta2 = resta(a,c)
            resta3 = resta(b,a)
            resta4 = resta(b,c)
            resta5 = resta(c,a)
            resta6 = resta(c,b)
            print("A - B = \n", resta1)
            print("A - C = \n", resta2)
            print("B - A = \n", resta3)
            print("B - C = \n", resta4)
            print("C - A = \n", resta5)
            print("C - B = \n", resta6)
        elif opcion == "4":
            complemento1 = compl(a,u)
            complemento2 = compl(b,u)
            complemento3 = compl(c,u)
            print("A complemento = \n", complemento1)
            print("B complemento = \n", complemento2)
            print("C complemento = \n", complemento3)
        elif opcion == "5":
            print("Cardinalidad A: \n", card(a))
            print("Cardinalidad B: \n", card(b))
            print("Cardinalidad C: \n", card(c))
        elif opcion == "6":
            print("Es subconjunto A de B:", subcj(a,b))
            print("Es subconjunto A de C:", subcj(a,c))
            print("Es subconjunto B de A:", subcj(b,a))
            print("Es subconjunto B de C:", subcj(b,c))
            print("Es subconjunto C de A:", subcj(c,a))
            print("Es subconjunto C de B:", subcj(c,b))
        elif opcion == "7":
            print("Es Disjunto A de B:", disj(a,b))
            print("Es Disjunto A de C:", disj(a,c))
            print("Es Disjunto B de A:", disj(b,c))
        elif opcion == "8":
            graficar_venn(a,b,c)
        else:
            break

#ejecuta la función principal
main()









