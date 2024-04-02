from flask_restful import Resource
from flask import request

USUARIOS = {
     1:{'Nombre':'Juan', 'Apellido':'Pérez', 'Correo':'JuanPe15@outlook.com.ar', 'Telefono':'2613485490'},
     2:{'Nombre':'Sofia', 'Apellido':'Dalmante', 'Correo':'sofi_dalmante02@gmail.com', 'Telefono':'2613846570'},
     
}

CONFIGURACION = {
    'Modo':'Oscuro',
    'Idioma/s':['Español','Ingles'],
    'Pais':'Argentina'
    }

class Usuarios(Resource):
    def get(self):
        return USUARIOS, 200
    

class Usuario(Resource):
    def get(self,id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        
        #En caso de que no exista
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in USUARIOS:  # Verifica que exista el id de usuario recibido en la tabla de Usuarios
            del USUARIOS[int(id)]
            return 'Usuario eliminado correctamente',204
        
        #Si no existe
        return 'No existe el id', 404
    
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201
    

    def put(self,id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        
        #Si no existe
        return 'No existe el id', 404


class Configuracion(Resource):
    def get(self):
        return CONFIGURACION, 200
    
    def put(self):
        data = request.get_json()
        CONFIGURACION.update(data)
        return '', 201