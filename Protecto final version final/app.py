
from flask import Flask, jsonify, request, render_template, redirect
from Lista import Usuarios

app = Flask(__name__)

controllerUsuarios = Usuarios()
tareasMilagro = controllerUsuarios.lista_Milagro
tareasDiego = controllerUsuarios.lista_Diego
tareasJonathan = controllerUsuarios.lista_Jonathan

#Entregar Datos JSON (Get:Obtener Datos, Post:Guardar Datos, Put: Actualizar, Delete: Borrar)

#Muestra todas las listas en Crudo
@app.route('/Listas')#GET por defecto
def ping():
    mi_json = jsonify({"Tareas de Diego": tareasDiego, 
    "Tareas de Mila": tareasMilagro, 
    "Tareas de Jona": tareasJonathan})
    return mi_json


#Muestra la lista de cada uno por separado en HTML 
@app.route('/Diego', methods=['GET', 'POST'])
def getList():
    mi_json = jsonify({"Tareas de Diego": tareasDiego}) 
    return mi_json

@app.route('/Milagro', methods=['GET', 'POST'])
def getList1():
    mi_json = jsonify({"Tareas de Milagro": tareasMilagro}) 
    return mi_json

@app.route('/Jonathan', methods=['GET', 'POST'])
def getList2():
    mi_json = jsonify({"Tareas de Jonathan": tareasJonathan}) 
    return mi_json



#(app insomnia->Permite enviar y mostrar Datos a nuestras Rest API)

#Crear y agregar Datos
@app.route('/lista_Diego', methods=['POST'])
def addTarea():
    new_tarea = {
        "Tarea": request.json['Tarea'],
        "Dia": request.json['Dia'],
        "Hora": request.json['Hora']
    }
    tareasDiego.append(new_tarea)
    return jsonify({"Message": "Tarea Agregada...!!!", "Lista de Cosas por Hacer": tareasDiego})


@app.route('/lista_Milagro', methods=['POST'])
def addTarea1():
    new_tarea = {
        "Tarea": request.json['Tarea'],
        "Dia": request.json['Dia'],
        "Hora": request.json['Hora']
    }
    tareasMilagro.append(new_tarea)
    return jsonify({"Message": "Tarea Agregada...!!!", "Lista de Cosas por Hacer": tareasMilagro})


@app.route('/lista_Jonathan', methods=['POST'])
def addTarea2():
    new_tarea = {
        "Tarea": request.json['Tarea'],
        "Dia": request.json['Dia'],
        "Hora": request.json['Hora']
    }
    tareasJonathan.append(new_tarea)
    return jsonify({"Message": "Tarea Agregada...!!!", "Lista de Cosas por Hacer": tareasJonathan})

#Actualizar Datos
@app.route('/lista_Diego/<string:tarea>', methods=['PUT'])
def editTarea(tarea):
    tareaFound = [tareas for tareas in tareasDiego if tareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        tareaFound[0]['Tarea'] = request.json['Tarea']
        tareaFound[0]['Dia'] = request.json['Dia']
        tareaFound[0]['Hora'] = request.json['Hora']
        return jsonify({"Message": "Tarea Actualizada","Lista de Tareas": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})


@app.route('/lista_Milagro/<string:tarea>', methods=['PUT'])
def editTarea1(tarea):
    tareaFound = [tareas for tareas in tareasMilagro if tareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        tareaFound[0]['Tarea'] = request.json['Tarea']
        tareaFound[0]['Dia'] = request.json['Dia']
        tareaFound[0]['Hora'] = request.json['Hora']
        return jsonify({"Message": "Tarea Actualizada","Lista de Tareas": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})


@app.route('/lista_Jonathan/<string:tarea>', methods=['PUT'])
def editTarea2(tarea):
    tareaFound = [tareas for tareas in tareasJonathan if tareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        tareaFound[0]['Tarea'] = request.json['Tarea']
        tareaFound[0]['Dia'] = request.json['Dia']
        tareaFound[0]['Hora'] = request.json['Hora']
        return jsonify({"Message": "Tarea Actualizada","Lista de Tareas": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})


    
#Eliminar Datos
@app.route('/lista_Diego/<string:tarea>', methods=['DELETE'])
def deleteTarea(tarea):
    tareaFound = [tareas for tareas in tareasDiego] 
    for item in tareaFound: 
        if item == tarea:
            pass

    if(len(tareaFound) > 0):
        tareasDiego.remove(tareaFound[0])
        return jsonify({"Message": "Tarea Eliminada...","Lista de Tareas": tareasDiego })
    return jsonify({"Message": tareaFound})


@app.route('/lista_Milagro/<string:tarea>', methods=['DELETE'])
def deleteTarea1(tarea):
    tareaFound = [tareas for tareas in tareasMilagro] 
    for item in tareaFound: 
        if item == tarea:
            pass

    if(len(tareaFound) > 0):
        tareasMilagro.remove(tareaFound[0])
        return jsonify({"Message": "Tarea Eliminada...","Lista de Tareas": tareasMilagro })
    return jsonify({"Message": tareaFound})
   
@app.route('/lista_Jonathan/<string:tarea>', methods=['DELETE'])
def deleteTarea2(tarea):
    tareaFound = [tareas for tareas in tareasJonathan] 
    for item in tareaFound: 
        if item == tarea:
            pass

    if(len(tareaFound) > 0):
        tareasJonathan.remove(tareaFound[0])
        return jsonify({"Message": "Tarea Eliminada...","Lista de Tareas": tareasJonathan })
    return jsonify({"Message": tareaFound})
if __name__ == '__main__':
    app.run(debug=True, port=4000)