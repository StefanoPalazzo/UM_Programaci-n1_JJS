from flask_restful import Resource
from flask import request

NOTIFICACIONES = {
    1:{'usuario_id': 1, 'mensaje':'El libro que solicitaste ya esta disponible', 'fecha':'15/03/2024'},
    2:{'usuario_id': 2, 'mensaje':'El libro que solicitaste ya esta disponible', 'fecha':'15/03/2024'},
}


class Notificaciones(Resource):
    def get(self):
        return NOTIFICACIONES, 200
    
    def post(self):
        usuario = request.get_json()
        id = int(max(NOTIFICACIONES.keys()))+1
        NOTIFICACIONES[id] = usuario
        return NOTIFICACIONES[id], 201

    
    
    