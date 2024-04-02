from flask_restful import Resource
from flask import request

LIBROS = {
     1:{'Nombre':'El resplandor', 'Autor':'Stephen King', 'Publicacion':'1977', 'genero': 'Terror', 'editorial':'Debolsillo'},
     2:{'Nombre':'Inteligencia Emocional', 'Autor':'Daniel Golleman', 'Publicacion':'1995', 'genero': 'Autoayuda', 'editorial':'Kairos'},
     3:{'Nombre':'Einstein', 'Autor':'Barry Parker', 'Publicacion':'2016', 'genero': 'Biografia', 'editorial':'Ateneo'},
}


class Libros(Resource):
    def get(self):
        return LIBROS, 200
    

class Libro (Resource):
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        
        #En caso de que no exista
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in LIBROS:  # Verifica que exista el id de usuario recibido en la tabla de LIBROS
            del LIBROS[int(id)]
            return 'Libro eliminado correctamente',204
        
        #Si no existe
        return 'No existe el id', 404
    
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys()))+1
        LIBROS[id] = libro
        return LIBROS[id], 201
    

    def put(self,id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json()
            libro.update(data)
            return '', 201
        
        #Si no existe
        return 'No existe el id', 404

