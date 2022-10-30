#Importando  flask y algunos paquetes del mismo
from flask import Flask, render_template, request, redirect, url_for, jsonify
from confiDB import *  #Importando conexion BD


#Declarando el nombre de la aplicación e inicializando - crear la aplicación Flask
app = Flask(__name__)
application = app


#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM lenguajes ORDER BY name_lenguaje")
    mycursor.execute(querySQL)
    dataLenguajes = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return render_template('public/index.html', listaLenguajes = dataLenguajes)
   
 
#Creando un decorador para mi ruta de borrarLenguajes
@app.route('/borrar-lenguaje', methods=['GET', 'POST'])
def borrarLenguaje():
    
    if request.method == 'POST':
        idLenguaje    = request.form['idLenguaje']
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute('DELETE FROM lenguajes WHERE id=%s', (idLenguaje,))
        conexion_MySQLdb.commit()
        
        #Nota: retorno solo un json y no una vista para evitar refescar la vista
        return jsonify(dataR=["respuesta", 1])
        
   
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    


if __name__ == "__main__":
    app.run(debug=True, port=8000)

