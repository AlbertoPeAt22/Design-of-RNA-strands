from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
        
def obtenerGenporLocalidadGenomica(genoma,inicio,fin):
    x=inicio
    gen=""
    while(x<=fin):
        gen+=genoma[x]
        x+=1
    print("\n")
    print("---------------------------------------------".center(50))
    print(gen)
    print("---------------------------------------------".center(50))
    print("\n")
    return gen

#Obteniendo el Genoma para la busqueda por cadena de ADN
def obtenerGenomaParaCadenaADN():
    try:
        #Abriendo el archivo del Genoma de S.Pyogennes
        #infoGenetica=open("GCA_900475035.1/GCA_900475035.1_41965_F01_genomic.fna","r")
        
        #Abriendo el archivo del Genoma de Mycoplasma_genitalium
        infoGenetica=open("GCA_900475035.1_41965_F01_genomic.fna","r")
        
        #Excluyendo la primer línea de especificaciones, ya que no tiene nucleótidos
        infoGenetica.readline()
        genomaSPy=infoGenetica.read().replace('\n','')  
        return genomaSPy
    except Exception as e:
        print(e)
    else:
        print("Se ha recuperado la información genética correctamente.")
    finally:
        infoGenetica.close()

def obtenerGenomaParaNombreDeGen():
    try:
        #Abriendo el archivo del Genoma de S.Pyogennes
        #infoGenetica=open("GCF_900475035.1/cds_from_genomic.fna","r")
        #Abriendo el archivo del Genoma de S.Pyogennes
        infoGenetica=open("cds_from_genomic.fna","r")    
        genomaSPy=infoGenetica.read()
        return genomaSPy
    except Exception as e:
        print(e)
    else:
        print("Se ha recuperado la información genética correctamente.")
    finally:
        infoGenetica.close()
    
#DP01 -> 4.	El sistema busca en donde se encuentra el objetivo en el genoma
def busquedaDeLocalidadGenomica(genoma,cadenaADN="",nombreGEN=False):
        localidadGenomica=[]
        
        if(nombreGEN==False):  #Si no se recibe un argumento para nombreGen entonces buscar por cadenaADN
            
            #---> BÚSQUEDA POR CADENA DE ADN <---
            print("La cadena de ADN Objetivo es la siguiente: ",cadenaADN)
            localidadGenomicaAux=[]    #Coordenadas de donde se encuentra el GEN buscado, tomando en cuenta las distintas localidades genómicas 
            lonCadenaADN=len(cadenaADN)
            lonGenoma=len(genoma)
            print(lonCadenaADN)
            print(lonGenoma)
            x=0
            y=lonCadenaADN
            
            #Se hace una comparación por fuerza exhaustiva, RECORRIENDO los NUCLÉOTIDOS DE UNO en UNO
            #Para encontrar dentro del GENOMA, la(s) localidad(es) que coincidan con la CADENA DE ADN OBJETIVO
            while(y<=lonGenoma):
                gen=genoma[x:y]
                if(gen==cadenaADN):
                    localidadGenomicaAux.append([x,y-1])   
                x+=1
                y+=1
            
            #DP01 --> 4 Alterno 2. No se encontró el objetivo
            if(len(localidadGenomicaAux)==0):
                return False
                
            #Sólo hay una localidad genómica
            elif(len(localidadGenomicaAux)==1):   
                localidadGenomica.append(localidadGenomicaAux[0])
                print(f"Se trabajará con la localidad genómica [{localidadGenomica[0][0]}..{localidadGenomica[0][1]}]")
                 #Da los índices o coordenadas de la localidad genómica con la que se trabajará
                return localidadGenomica   
            
            #DP01 -> 4. ALTERNO 1. Se presentan varias localizaciones en el genoma con el objetivo de corte 
            else:
                #DP01 -> 4. A.1.1 El sistema muestra un informe de las localizaciones que repiten el objetivo.
                print("--->Se han encontrado varias localidades genómicas, seleccione aquellas con las que desea trabajar <---")
                
                #Imprimiendo el INFORME 
                x=1
                for coordenadas in localidadGenomicaAux:
                    print(f"{x}--> [{coordenadas[0]}..{coordenadas[1]}]")
                    x+=1
                #DP01 ---> 4 A1.2. El usuario selecciona la(s) localización(es) en las que se quiere enfocar.
                opciones=input("Opciones: ") 
                print(opciones)
                
                y=0 
                #Añadiendo las localidades genómicas con las cuales trabajar
                for indice in opciones: 
                    localidadGenomica.append(localidadGenomicaAux[int(indice)-1]) 
                    
                print("--->Se trabajará con las siguientes localidades genómicas: <---") 
                print(localidadGenomica)
                return localidadGenomica  #Da los índices de la(s) localidad(es) genómica(s) con la(s) que se trabajará
                
        else:
            # ----> BÚSQUEDA POR NOMBRE DE GEN <---
            #Buscando el nombre del GEN dentro del genoma con encabezados
            print("El nombre del gen objetivo es el siguiente: ",nombreGEN)
            posicion1=genoma.find("[gene="+nombreGEN+"]")  
            if(posicion1!=-1):
                print(f"La subcadena se encuentra en la posición: {posicion1}")
                x=posicion1
                infoDelGen=""  
                while(genoma[x]!='\n'):  
                    infoDelGen+=genoma[x]
                    x+=1
                print(infoDelGen)
                
                posicion2=infoDelGen.find("location=")
                print(f"La subcadena se encuentra en la posición: {posicion1+posicion2}")
                #Se debe de considerar la posición 1 y la posición 2
                x=posicion2+posicion1
                primeraCoordena=""
                segundaCoordenada=""
                
                # Se busca la cadena dentro del encabezado de la forma: [location=1..1356]
                #Se guarda la primera cadena cuando se encuentre el caracter "."
                while(genoma[x]!="."):  
                    try:
                        if isinstance(int(genoma[x]),int):
                            primeraCoordena+=genoma[x]
                    except Exception as e:
                        pass
                    x+=1
                
                #Ha encontrado un punto, recorremos otro [location=1..1356], recorremos el segundo punto para 
                #comenzar a encontrar la segunda coordenada
                x+=1
                while(genoma[x]!="]"):
                    try:
                        if isinstance(int(genoma[x]),int):
                            segundaCoordenada+=genoma[x]
                    except Exception as e:
                        pass
                    x+=1
                
                print("Primer coordenada: ",primeraCoordena)
                print("Segunda coordenada: ",segundaCoordenada)
                
                #Castear las coordenadas por ser del tipo STRING 
                primeraCoordena=int(primeraCoordena)
                segundaCoordenada=int(segundaCoordenada)
                
                #Restar uno a las coordenadas para que estas sean tratadas en notación de arrays de 0 a n
                primeraCoordena-=1
                segundaCoordenada-=1
                localidadGenomica.append([primeraCoordena,segundaCoordenada])
                print(f"Se trabajará con la localidad genómica [{localidadGenomica[0][0]}..{localidadGenomica[0][1]}]")
                return localidadGenomica
            else:
                return False
            
def busquedaSecuenciasPAMCirc(genoma,localidadGenomica):
    
    #Recorriendo el genoma pero con las posiciones de la localidadGenómica 
    locGenConSecuenciasPAM=[]    #Localidad genómica con secuencias PAM adyacentes
    longGenoma=len(genoma)
    inicio=0
    fin=0
    secPAMAux=""
    secADNAdyacentesAPAM=[] 
    ARNAux=""
    arnAuxInd=0
    longARN=18  #Se puede modificar hasta 23 
    numIteraciones=1
    numDeLocalidad=1    #Variable que sirve como ID de cada localidad genómica, INICIA DESDE 1
    
    #Búscar Secuencias PAM mediante FUERZA EXHAUSTIVA DENTRO DE LA LOCALIDAD GENÓMICA
    for coordenadas in localidadGenomica:   #Varias LOCALIDADES GENÓMICAS
        inicio=coordenadas[0]   #Coordenada de inicio de la localidad genómica
        fin=coordenadas[1]      #Coordenada de fin de la localidad genómica, 0..N
        
        while(inicio<=fin-2):  
            secPAMAux=genoma[inicio:inicio+3]   
            #Encontrando la secuencia PAM
            if(secPAMAux=="AGG" or secPAMAux=="TGG" or secPAMAux=="CGG" or secPAMAux=="GGG"):
                locGenConSecuenciasPAM.append(inicio)  
                print(f"Se ha añadido la coordenada {inicio} que es donde inicia la secuencia PAM: {secPAMAux}")
                arnAuxInd=inicio-1
                
                # --->GENERACIÓN DEL ARN UNA VEZ ENCONTRADA LA SECUENCIA PAM De Derecha a Izquierda<---
                print("***Se empezará a generar un ARN desde la posición: ",arnAuxInd, "hacia atrás***")
                while(arnAuxInd>=0 and numIteraciones<=longARN):    
                    ARNAux+=genoma[arnAuxInd]
                    numIteraciones+=1   #Se cuenta el número de iteraciones
                    arnAuxInd-=1        #Se va hacia la izquierda, después de encontrar ese segmento de ADN
                    if(len(ARNAux)>=longARN):
                        #Voltear la cadena de nucleótidos, para que se conserve la forma del SEGMENTO DE ADN
                        ARNAux=ARNAux[::-1]
                        secADNAdyacentesAPAM.append([[inicio-longARN,inicio-1],ARNAux,numDeLocalidad])    
                numIteraciones=1   
                ARNAux=""      
            inicio+=1   
        numDeLocalidad+=1
    
    #Buscar secuencias PAM dentro de todo el GENOMA, guardando índices y por FUERZA EXHAUSTIVA
    indicesSecPAM=[]
    indexInicio=0
    for secPAM in genoma: 
        if(indexInicio<=longGenoma-3):  
            secPAM=genoma[indexInicio:indexInicio+3]    #Tomando genes de longitud 3
            if(secPAM=="AGG" or secPAM=="TGG" or secPAM=="CGG" or secPAM=="GGG"):
                indicesSecPAM.append([indexInicio,indexInicio+2,secPAM])    
            indexInicio+=1  #Avanzar de UN NECLEÓTIDO EN UN NUCLÉOTIDO
    print("\n\n")
    print("\nNúmero de secuencias PAM encontradas en todo el genoma",len(indicesSecPAM))
    print("\nNúmero de ARNs encontrados en el ADN Objetivo: ",len(secADNAdyacentesAPAM))
    return [secADNAdyacentesAPAM,indicesSecPAM]   #Retorna los genes complementarios a los ARNS y las localidades genómicas de las secuencias PAM dentro de todo el GENOMA
    
def obtencionARNsComplementarios(secADNAdyacentesAPAM):
    ARNsComplementarios=[]
    secuencia=""
    ARNComplem=""
    
    print("--->Genes y sus respectivos ARNS complementarios <---".center(50))
    for adn in secADNAdyacentesAPAM:
        #
        print(adn[1])
        secuencia=Seq(adn[1])
        ARNComplem=str(secuencia.complement_rna())  #Usando una función de Biopython y castenado a String
        print(ARNComplem,"\n")
        ARNsComplementarios.append([adn[0],ARNComplem,adn[2]]) 
    return ARNsComplementarios

def similitudDeGenes(gen,genObjetivo,porcentaje):
    porcentajeSimilitudMinimo=porcentaje #Se puede variar este umbral 
    porcentajeSimilitudGenes=0
    numNucleotidosIguales=0 #Si tiene 18 nucleótidos(puede variar a 23) iguales tiene un 100% de similitud
                            #El 18 puede variar, de acuerdo al tamaño del ARN
    x=0
    for nucleotido in genObjetivo:
        if(nucleotido==gen[x]):
            numNucleotidosIguales+=1
        x+=1
        
    porcentajeSimilitudGenes=(numNucleotidosIguales*100)/len(gen)
    
    if(porcentajeSimilitudGenes>=porcentajeSimilitudMinimo):
        return True
    else:
        return False

def obtenerPorcentajeDeGC(gen):
    porcentajeGC=0
    longiGen=len(gen)
    cantidadDeNucleGC=0
    for nucleotido in gen:
        if(nucleotido=="G" or nucleotido=="C"):
            cantidadDeNucleGC+=1
    porcentajeGC=(cantidadDeNucleGC*100)/longiGen
    return porcentajeGC
    
def analisisARNsComplementarios(genoma,cadenasDeARN,locaGenomicasSecPAM):
    lonGenoma=len(genoma)
    lonARNcomp=len(cadenasDeARN[0][1])
    print(lonGenoma)
    print(lonARNcomp)
    x=0
    y=lonARNcomp
    secuenciaARN=""    #Objeto necesario para trabajar con Objetos de Biopython
    genObjetivo=""
    genAux=""
    ARNsAux=[]
    datosARNsAux=[]
    numGenesSimilaresOffTarget=0
    porcentajeSimilitud=60
    ARNsProcesadosDistintasPrecisiones=[]        #Arreglo que trae los ARNs con 3 distintas precisiones de similitud
    ARNsProcesados=[]                            #Gen base del ARN, ARN, Sitios offtarget, contenido de GC
    ARNsProcesadosAux=[]
    #Análisis de ARNs guía con 3 precisiones de similitud de los ARN, VA DECREMENTALMENTE -5%, -5% y -5%
    for x in range(3):
        print(f"\n\n\n---->Analisis de los ARN's con {porcentajeSimilitud}% de precisión<-------")
        
        #Recorre una lista de elementos que contiene: coordenadas del gen complementario al ARN, el ARN y la localidad genómica
        for cadenaARN in cadenasDeARN:
            
        #Comparar los genes complementarios a los ARN para encontrar posibles sitios Off-target
        #La búsqueda se hace fuera del segmento de ADN o gen Objetivo, en todo el genoma    
            secuenciaARN=Seq(cadenaARN[1])
            genObjetivo=str(secuenciaARN.back_transcribe().complement())
            porcentajeGC=obtenerPorcentajeDeGC(cadenaARN[1])
            print("--------------------------------".center(50))
            print("Gen base del ARN, objetivo: ",genObjetivo) 
            print("ARN: ",cadenaARN[1])
            ARNsProcesadosAux.append(genObjetivo)       #Guardando el gen base para la creación del ARN
            ARNsProcesadosAux.append(cadenaARN[1])      #Guardando el ARN generado con el anterior gen 
            
            #--->Buscando sitios off-target con LOCACIONES GENÓMICAS DE LAS SECUENCIAS PAM<----
            indiceAux=0
            numComparaciones=0
            genParaARNAux=""
            inicioAux=0
            finAux=0

            for localidadGen in locaGenomicasSecPAM:
                #Generando los genes que pueden ser off-target

                finAux=localidadGen[0] #Coordenada de inicio de una secuencia PAM, pero es la final para un ARN de N de longitud
                                            
                inicioAux=finAux-lonARNcomp #Coordenada de INICIO de una secuencia de ARN
                if(inicioAux>=0):
                    genParaARNAux=genoma[inicioAux:finAux]  #Recordar que es finAux-1
                    if(similitudDeGenes(genParaARNAux,genObjetivo,porcentajeSimilitud)):
                        ARNsAux.append([genParaARNAux,inicioAux,finAux-1])  

            print("Número de sitios de Off-target: ",len(ARNsAux)-1) 
            print(f"El ARN '{cadenaARN[1]}' tiene: {porcentajeGC:.3f}% de contenido GC")
            print(f"Localidad genómica: {cadenaARN[2]}")  #Manejar localidades genómicas con numeración del 1 al N
            ARNsProcesadosAux.append(len(ARNsAux)-1)    #Guardando sitios off-target
            ARNsProcesadosAux.append(porcentajeGC)      #Guardando porcentaje GC
            ARNsProcesadosAux.append(cadenaARN[2])
            ARNsProcesadosAux.append(cadenaARN[0][0])   #Guardando la coordenada de inicio del Gen Complementario al ARN
            ARNsProcesadosAux.append(cadenaARN[0][1])   #Guardando la coordenada de fin del Gen Complementario al ARN
            ARNsProcesados.append(ARNsProcesadosAux)    
            ARNsAux=[]   #Limpiar los auxiliares para una nueva búsqueda de un ARN
            ARNsProcesadosAux=[]    #Limpiar este array 
        
        ARNsProcesadosDistintasPrecisiones.append([porcentajeSimilitud,ARNsProcesados]) #Se guarda el porcentaje de similitud y los ARNsProcesados
        ARNsProcesados=[]
        porcentajeSimilitud+=5  #Incrementar de 5 en 5 el porcentaje de similitud
        
    return ARNsProcesadosDistintasPrecisiones

def imprimirInformacionARNFiltradoporGC(ARNsFiltrados):
    for datos in ARNsFiltrados:
        print("Gen base del ARN, objetivo: ",datos[0]) 
        print("ARN: ",datos[1])
        print(f">>>>>Tiene: {datos[3]:.3f}% de contenido GC<<<<<")
        print("Número sitios de Off-target: ",datos[2]) 
        print(f"Localidad genómica: ", datos[4],"\n")

def imprimirInformacionARNFiltradoPorSitOffTarget(ARNsFiltrados):
    for datos in ARNsFiltrados:
        print("Gen base del ARN, objetivo: ",datos[0]) 
        print("ARN: ",datos[1])
        print(">>>>>Número sitios de Off-target: ",datos[2],"<<<<<") 
        print(f"Tiene: {datos[3]:.3f}% de contenido GC")
        print(f"Localidad genómica: ", datos[4],"\n")

def mostradoYFiltradoDeResultados(ARNsProcesados,opcion):
    numIteraciones=len(ARNsProcesados)  #Número de iteraciones de acuerdo a la precisión de similitud de ARNs con los sitios off-target
    #print(numIteraciones)
    if(opcion=="1"):  #Filtrar por GC
        DatosARNs=ARNsProcesados[0][1]  #
        print(f"\n\n---->Datos Filtrados por contenido GC<----")
        print("Ordenados de Mayor a Menor por que entre más porcentaje de GC, MEJOR")
        ARNsFiltradosPorGC=sorted(DatosARNs,key=lambda x: x[3],reverse=True)
        imprimirInformacionARNFiltradoporGC(ARNsFiltradosPorGC)
        return ARNsFiltradosPorGC        
    
    elif(opcion=="2"):  #Filtrar por sitios off-target
        ARNsFiltradosPorSitOffTarget=[]
        for i in range(numIteraciones):
            precision=ARNsProcesados[i][0]  
            DatosARNs=ARNsProcesados[i][1]  
            print(f"\n\n---->Datos Filtrados por Cantidad de Sitios Off-Target y con {precision}% de precision<----")
            print("Ordenados de Menor a Mayor por que entre menos Sitios Off-Target, MAYOR PRECISIÓN DEL ARN")
            ARNsFiltradosPorSitOffTargetAux=sorted(DatosARNs,key=lambda x: x[2],reverse=False)
            imprimirInformacionARNFiltradoPorSitOffTarget(ARNsFiltradosPorSitOffTargetAux)
            ARNsFiltradosPorSitOffTarget.append([precision,ARNsFiltradosPorSitOffTargetAux])
        
        return ARNsFiltradosPorSitOffTarget

    else:
        return False