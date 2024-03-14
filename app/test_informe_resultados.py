from informe_resultados import son_apareables, tiene_apareamiento, verificar_apareamiento

def test_son_apareables():
    assert son_apareables("A", "U")
    assert son_apareables("G", "C")
    assert son_apareables("AC", "GU")
    assert son_apareables("AAGC", "GCUU")
    #Ahora probamos que no sean apareables
    assert not son_apareables("A", "A")
    assert not son_apareables("G", "G")
    assert not son_apareables("AC", "AC")