from flask import Flask, request, render_template, redirect, url_for, send_file
from mainProgram import *
from busquedaBLAST import *
import aspose.pdf as ap
app=Flask(__name__)
ARNSProcesadosGlobal=""
app.config['globalVar']=""
app.config['globalVarGC']=""
app.config['globalVarOff']=""

@app.route('/')
def inicio():    
    return redirect(url_for('index'))

@app.route('/inicio', methods=['GET','POST'])
def index(): 
    cadena= request.form.get('cadena')
    print(cadena)   
    return render_template('index.html',noADNObj=False,noARNs=False,noNombreGen=False)    

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/descargar')
def descargar():
    if(app.config['globalVar']!=""):        
        # Initialize document object
        document = ap.Document()
        listARNS = app.config['globalVar']
    
        # Add page
        page = document.pages.add()
        GCConFormato=""
        for i in listARNS:
            # Titulo
            page.paragraphs.add(ap.text.TextFragment(" "))
            page.paragraphs.add(ap.text.TextFragment("Análisis de los ARN's con " + str(i[0]) + "%" + "de similitud respecto a sitios off-target"))
            page.paragraphs.add(ap.text.TextFragment(" "))
            # Tabla
            # Create a table
            table = ap.Table()

            # Set border width 
            table.default_cell_border =  ap.BorderInfo(ap.BorderSide.ALL, 0.3, ap.Color.black)

            # Add a row to the table
            row = table.rows.add()
            # Titulos
            #row.cells.add('#')
            row.cells.add('Secuencia Objetivo')
            row.cells.add('Locacion Genomica')
            row.cells.add('Contenido de GC (%)')
            row.cells.add('No.De Sitios off-target')
            
            for j in i[1]:
                row2 = table.rows.add()
            #row2.cells.add(str(b))
                row2.cells.add(str(j[1]))
                row2.cells.add(str(j[5]) + ":" + str(j[6]))
                GCConFormato="{:.2f}".format(j[3])
                row2.cells.add(GCConFormato)
                row2.cells.add(str(j[2]))
                #b += 1 Esta solo es para añadir el numeral

            page.paragraphs.add(ap.text.TextFragment(" "))
            page.paragraphs.add(table)

        # Save updated PDF
        document.save("Cadenas.pdf")

        return send_file('Cadenas.pdf')
    else:
            # Initialize document object
        document = ap.Document()

        # Add page
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("El archivo está vacío."))
        page.paragraphs.add(ap.text.TextFragment(" "))

        # Save updated PDF
        document.save("Cadenas.pdf")

        return send_file('Cadenas.pdf')

@app.route('/descargarGC')
def descargarGC():       
    if(app.config['globalVarGC']!=""):
        
        # Initialize document object
        document = ap.Document()
        listARNS = app.config['globalVarGC']
        
        # Add page
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("ARNs filtrados por porcentaje de GC (Guanina y Citosina)"))
        page.paragraphs.add(ap.text.TextFragment(" "))
        
            # Tabla
            # Create a table
        table = ap.Table()

            # Set border width 
        table.default_cell_border =  ap.BorderInfo(ap.BorderSide.ALL, 0.3, ap.Color.black)

            # Add a row to the table
        row = table.rows.add()
            # Titulos
            #row.cells.add('#')
        row.cells.add('Secuencia Objetivo')
        row.cells.add('Locacion Genomica')
        row.cells.add('Contenido de GC (%)')
        row.cells.add('No.De Sitios off-target')
        GCConFormato=""
        
        for j in listARNS:
            row2 = table.rows.add()
            #row2.cells.add(str(b))
            row2.cells.add(str(j[1]))
            row2.cells.add(str(j[5]) + ":" + str(j[6]))
            GCConFormato="{:.2f}".format(j[3])
            row2.cells.add(GCConFormato)
            row2.cells.add(str(j[2]))
                #b += 1 Esta solo es para añadir el numeral

        page.paragraphs.add(ap.text.TextFragment(" "))
        page.paragraphs.add(table)

        # Save updated PDF
        document.save("CadenasGC.pdf")

        return send_file('CadenasGC.pdf')
    else:
            # Initialize document object
        document = ap.Document()

        # Add page
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("El archivo está vacío."))
        page.paragraphs.add(ap.text.TextFragment(" "))

        # Save updated PDF
        document.save("CadenasGC.pdf")

        return send_file('CadenasGC.pdf')
    
@app.route('/descargarOff')
def descargarOff():
    if(app.config['globalVarOff']!=""):        
        # Initialize document object
        document = ap.Document()
        listARNS = app.config['globalVarOff']
    
        # Add page
        page = document.pages.add()

        for i in listARNS:
            # Titulo
            page.paragraphs.add(ap.text.TextFragment(" "))
            page.paragraphs.add(ap.text.TextFragment("Análisis de los ARN's con " + str(i[0]) + "%" + "de similitud respecto a sitios off-target"))
            page.paragraphs.add(ap.text.TextFragment(" "))
            # Tabla
            # Create a table
            table = ap.Table()

            # Set border width 
            table.default_cell_border =  ap.BorderInfo(ap.BorderSide.ALL, 0.3, ap.Color.black)

            # Add a row to the table
            row = table.rows.add()
            # Titulos
            #row.cells.add('#')
            row.cells.add('Secuencia Objetivo')
            row.cells.add('Locacion Genomica')
            row.cells.add('Contenido de GC (%)')
            row.cells.add('No.De Sitios off-target')
            GCConFormato=""
            for j in i[1]:
                row2 = table.rows.add()
            #row2.cells.add(str(b))
                row2.cells.add(str(j[1]))
                row2.cells.add(str(j[5]) + ":" + str(j[6])) 
                GCConFormato="{:.2f}".format(j[3])
                row2.cells.add(GCConFormato)
                row2.cells.add(str(j[2]))
                #b += 1 Esta solo es para añadir el numeral

            page.paragraphs.add(ap.text.TextFragment(" "))
            page.paragraphs.add(table)

        # Save updated PDF
        document.save("CadenasOff.pdf")

        return send_file('CadenasOff.pdf')
    else: 
        document = ap.Document()

        # Add page
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("El archivo está vacío."))
        page.paragraphs.add(ap.text.TextFragment(" "))

        # Save updated PDF
        document.save("CadenasOff.pdf")

        return send_file('CadenasOff.pdf')
        
@app.route('/fac_questions')
def fac():
    return render_template('fac_questions.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/post1')
def post1():    
    return render_template('post1.html')

@app.route('/post2')
def post2():    
    return render_template('post2.html')

@app.route('/post3')
def post3():    
    return render_template('post3.html')

@app.route('/resultados', methods=['GET','POST'])
def resultados():
    cadena= request.form.get('cadena')
    if(cadena!=None):    
        if(len(cadena)<20):
            genomaSPy1=obtenerGenomaParaNombreDeGen() 
            localidadesGenomicas=busquedaDeLocalidadGenomica(genomaSPy1,"", cadena)
            if(localidadesGenomicas!=False):
                genomaSPy2=obtenerGenomaParaCadenaADN() #Al final de cuentas, ambas búsquedas trabajan con un mismo archivo.fda
                obtenerGenporLocalidadGenomica(genomaSPy2,localidadesGenomicas[0][0],localidadesGenomicas[0][1])  #La localidad genómica es un ARRAY
                secParaARN,indicesLocalidadesGenomicaSecPAM=busquedaSecuenciasPAMCirc(genomaSPy2,localidadesGenomicas) 
                if(len(secParaARN)>0):
                    arnsComplementarios=obtencionARNsComplementarios(secParaARN)
                    ARNsProcesados=analisisARNsComplementarios(genomaSPy2,arnsComplementarios,indicesLocalidadesGenomicaSecPAM)
                    app.config["globalVar"]=ARNsProcesados
                    ARNSProcesadosGlobal=app.config["globalVar"]
                    return render_template('resultados.html',ARNsProcesados=ARNSProcesadosGlobal)
                    #mostradoYFiltradoDeResultados(ARNsProcesados)
                else: 
                    print("\nNo se han encontrado ARNs dentro del segmento de ADN correspondiente al nombre de Gen ingresado")
                    return render_template('index.html',noADNObj=False,noARNs=True,noNombreGen=False)
            else:
                print("\nNo se ha encontrado el nombre de Gen ingresado.")
                return render_template('index.html',noADNObj=False,noARNs=False,noNombreGen=True)
        else:
            genomaSPy=obtenerGenomaParaCadenaADN()
            localidadesGenomicas=busquedaDeLocalidadGenomicaBLAST(genomaSPy,cadena)    #Búsqueda por cadena de ADN
            print(f"Se trabajará con la localidad genómica: [{localidadesGenomicas[0][0]}..{localidadesGenomicas[0][1]-1}]")
            if(localidadesGenomicas!=False):
        #Secuencia Complementaria a ARN en ADN objetivo tiene las localidades genómicas de los genes complementarios dentro del objetivo y el PROPIO GEN   
                secCompARNEnADNObjetivo,indicesLocalidadesGenomicaSecPAM=busquedaSecuenciasPAMCirc(genomaSPy,localidadesGenomicas)
                if(len(secCompARNEnADNObjetivo)>0):   #Validación para continuar 
                    arnsComplementarios=obtencionARNsComplementarios(secCompARNEnADNObjetivo)
                    ARNsProcesados=analisisARNsComplementarios(genomaSPy,arnsComplementarios,indicesLocalidadesGenomicaSecPAM)
                    app.config["globalVar"]=ARNsProcesados
                    ARNSProcesadosGlobal=app.config["globalVar"]
                    return render_template('resultados.html',ARNsProcesados=ARNSProcesadosGlobal)
                    #mostradoYFiltradoDeResultados(ARNsProcesados)
                else: 
            #Mostrar en pantalla que no existen ARNs para analizar 
                    print("\nNo se han encontrado ARNs dentro de la cadena de ADN Objetivo ingresada")
                    return render_template('index.html',noADNObj=False,noARNs=True,noNombreGen=False)
            else:
                print("\nNo se ha encontrado la cadena de ADN Objetivo ingresada")
                return render_template('index.html',noADNObj=True,noARNs=False,noNombreGen=False)
        
    else:
        return redirect(url_for('inicio'))
    
@app.route('/resultadosGC')
def resultadosGC():
    opcion=request.args.get('opcion')
    if(opcion!=None and opcion=="1"):
        #print(opcion,type(opcion))
        #print("Longitud",len(app.config['globalVar']))
        if(app.config['globalVar']!=""):
            ARNsFiltradosGC=mostradoYFiltradoDeResultados(app.config['globalVar'],opcion)
            app.config['globalVarGC'] = ARNsFiltradosGC
            return render_template('resultadosGC.html',ARNsFiltradosGC=ARNsFiltradosGC)
        else:
            return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))
    
@app.route('/resultadosSitOffTarget')
def resultadosSitOffTarget():
    opcion=request.args.get('opcion')
    if(opcion!=None and opcion=="2"):
        #print(opcion,type(opcion))
        #print("Longitud",len(app.config['globalVar']))
        if(app.config['globalVar']!=""):
            ARNsFiltradosOffTarg=mostradoYFiltradoDeResultados(app.config['globalVar'],opcion)
            app.config['globalVarOff'] = ARNsFiltradosOffTarg
            return render_template('resultadosSitOffTarget.html',ARNsFiltradosOffTarg=ARNsFiltradosOffTarg)
        else:
            return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))
    
@app.errorhandler(404)
def pageNotFound(error):
    return redirect(url_for('inicio'))

if __name__=='__main__':
    app.run(debug=True,port=8000)
    
