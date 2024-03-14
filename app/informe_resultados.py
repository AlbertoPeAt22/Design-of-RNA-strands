apareamientos = []
tamaño_entrada = 18

def son_apareables(cadena1, cadena2):
    tamaño_cadenas = len(cadena1) # Ambas cadenas tienen el mismo tamaño
    coincidencias = 0
    apareables = False

    for x in range(tamaño_cadenas):
        if (((cadena1[x] == "A") and (cadena2[tamaño_cadenas - 1 - x] == "U")) or ((cadena1[x] == "G") and (cadena2[tamaño_cadenas - 1 -x] == "C")) or ((cadena1[x] == "C") and (cadena2[tamaño_cadenas -1 -x] == "G")) or ((cadena1[x] == "U") and (cadena2[tamaño_cadenas - 1 -x] == "A"))):
            coincidencias += 1
        if coincidencias == tamaño_cadenas:
            apareables = True
    return apareables


def tiene_apareamiento(cadena):
    for tamaño_cadena in range(4,10):
        inicio_cadena_uno = 0
        inicio_cadena_dos = inicio_cadena_uno + tamaño_cadena

        while(not son_apareables(cadena[inicio_cadena_uno:inicio_cadena_uno + tamaño_cadena -1], cadena[inicio_cadena_dos:inicio_cadena_dos + tamaño_cadena -1])):
            if inicio_cadena_dos + tamaño_cadena -1 >= tamaño_entrada -1:
                if inicio_cadena_uno == inicio_cadena_dos - tamaño_cadena:
                    break
                else:
                    inicio_cadena_uno += 1
                    inicio_cadena_dos = inicio_cadena_uno + tamaño_cadena
            else:
                inicio_cadena_dos += 1
        
        if son_apareables(cadena[inicio_cadena_uno:inicio_cadena_uno + tamaño_cadena -1], cadena[inicio_cadena_dos:inicio_cadena_dos + tamaño_cadena -1]):
            #Agregar las cadenas y su posición a un diccionario
            apareamiento = {"inicio_cadena_uno":inicio_cadena_uno, "inicio_cadena_dos": inicio_cadena_dos, "cadena_uno": cadena[inicio_cadena_uno: inicio_cadena_uno + tamaño_cadena -1], "cadena_dos": cadena[inicio_cadena_dos:inicio_cadena_dos + tamaño_cadena -1]}
            apareamientos.append(apareamiento)

def verificar_apareamiento(lista_cadenas):
    for cadena in lista_cadenas:
        tiene_apareamiento(cadena)        
    #imprimir los apareamientos
    if len(apareamientos) == 0:
        print("No hay apareamientos")
    else:
        for x in range(len(apareamientos)):
            print("Apareamiento # ", x)
            for clave, valor in apareamientos[x].items():
                print(clave,valor)
            print("\n")

# Ejemplo de uso
PIM_01 = ['ACUUGGUACACGCAGAGU', 'CCUUCUUAGGACGCGAUU', 'UACUACGGACUAUUCUAU' , 'GGAAGGAAAAACUGGUUU', 'UUUAUAGGCGGUUCUAUA', 'UGCUAGUGUAGGCGAAGA', 'ACCGAUUGGGGAAAAUUU', 'ACUUACAACAGACAAGGA', 'GAUUUAGUAUUCGCAUCU', 'ACCAAAAUCGUGGAUCAU', 'AUCGUGGAUCAUUCCUUG', 'UUCCUUGACCGUUAGCUC', 'AGCUCUCCUGUGGACUAG', 'UGACAGAGUGGUGGUGCU', 'UGAACAAGAUCUCGUUUC', 'UCUCCGAGUAGAAUCAAC', 'CUCCGAGUAGAAUCAACA', 'ACAGGGUUUACGGUAAGG', 'CAGUAUUAGACAGGUUGA', 'AGUAUUAGACAGGUUGAU', 'GACAGGUUGAUCCCUGUU', 'UAGUACGCACUACGCUCG', 'GGCGAUUGACAAGUAAUU', 'GCGGUUUAAUCAUGAUGA', 'CGGUUUAAUCAUGAUGAA', 'AUCAUGAUGAACCCAUUA', 'UAGUCUGACGAGGUGUAG', 'AGUCUGACGAGGUGUAGA', 'CCCAUAUUGAGGGGUUUC', 'AGGCGCUAUCGCUGGGGA'] #Cadenas de la prueba de implantación 1 PIM-01

PIM_02 = ['GUUAAUGCAUUCUAUCGG', 'UCGAAGAGCAUAGUUUAG', 'UUCUAGAAGAUUGAGUUU', 'AGUUGAUUAGCAAACUUU', 'AUUAGCAAACUUUACCAA', 'GUUUGUUAACUAGAUUGA', 'UAGAUUGAACCGAUUGUG', 'CGCGUACUCGUUAAACUG', 'GCGUACUCGUUAAACUGA', 'GAAACAUUACUUUUUCGU', 'UACUUUUUCGUUCCGUGA', 'ACUUUUUCGUUCCGUGAA'] #Cadenas de la prueba de implantación 2 PIM-02

PIM_03 = ['UGGGUUUGAAUAUACUGU', 'GCGAGAUCAGGAGAGUGG', 'UCAGGAGAGUGGACCAGG', 'GAGAGUGGACCAGGACCA', 'GACCAGGACCAACCGGGU', 'GGUUUGUUUUGGAUAGAA', 'GAUAGAAUCCUCACACAG', 'AUAGAAUCCUCACACAGA', 'UCGCUAGCGACUUUGUAA', 'CGCUAGCGACUUUGUAAU', 'GCUAGCGACUUUGUAAUC', 'CUAGCGACUUUGUAAUCC', 'AUCCCCCUUGGAAUGCGA', 'CCGGUUUGCGCAGUACGU', 'CGGUUUGCGCAGUACGUA', 'UUCGUGGUAACUUUGCGU', 'CGAUGGUAAGGUAGCAAC', 'ACACCUAGUCAAUGGUUU', 'CACUGCUAGUUCUUUAGU', 'GGUGUGGGACGGUGAAAA', 'GUGUGGGACGGUGAAAAA', 'UAAAGUGGGUCUUUCGUA', 'UUCGUAGCCUUGAGGACU']

resultados = verificar_apareamiento(PIM_03)
print(resultados)
