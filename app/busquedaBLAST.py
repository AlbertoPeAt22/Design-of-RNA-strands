from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import MutableSeq

def busquedaDeLocalidadGenomicaBLAST(genoma, cadenaADNObjetivo):
    # Crear una secuencia Bio.Seq a partir del genoma
    secuencia_genoma = Seq(genoma)

    # Crear un objeto MutableSeq para poder buscar la cadena objetivo
    mutable_genoma = MutableSeq(str(secuencia_genoma))

    # Convertir la cadenaADNObjetivo en una secuencia Bio.Seq
    secuencia_objetivo = Seq(cadenaADNObjetivo)

    # Buscar la cadenaADNObjetivo en el genoma
    resultadosAux = []
    resultados=[]
    while mutable_genoma.find(secuencia_objetivo) != -1:
        indice_inicio = mutable_genoma.find(secuencia_objetivo)
        indice_final = indice_inicio + len(secuencia_objetivo)
        resultadosAux.append((indice_inicio, indice_final))
        mutable_genoma[indice_inicio:indice_final] = 'N' * len(secuencia_objetivo)
    
    if(len(resultadosAux)>0):
        resultados.append(resultadosAux[0])
        return resultados
    else:
        return False