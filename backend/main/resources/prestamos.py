from flask_restful import Resource
from flask import request

PRESTAMOS = {
     1:{'usuario_id': 2, 'Libro_id':2, 'fecha_prestamo':'15/03/2024', 'fecha_devolucion':'15/04/2024', 'estado':'en prestamo'},
     2:{'usuario_id': 1, 'Libro_id':3, 'fecha_prestamo':'29/03/2024', 'fecha_devolucion':'29/04/2024', 'estado':'en prestamo'},
}


class Prestamos(Resource):
    def get(self):
        return PRESTAMOS, 200

class Prestamo(Resource):
    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        
        #En caso de que no exista
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in PRESTAMOS:  # Verifica que exista el id de usuario recibido en la tabla de Usuarios
            del PRESTAMOS[int(id)]
            return 'Usuario eliminado correctamente',204
        
        #Si no existe
        return 'No existe el id', 404
    
    def post(self):
        usuario = request.get_json()
        id = int(max(PRESTAMOS.keys()))+1
        PRESTAMOS[id] = usuario
        return PRESTAMOS[id], 201
    

    def put(self,id):
        if int(id) in PRESTAMOS:
            usuario = PRESTAMOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        
        #Si no existe
        return 'No existe el id', 404

