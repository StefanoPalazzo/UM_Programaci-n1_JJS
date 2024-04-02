from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

# Inicializamos restful
api = Api()



# Este metodo create_app inicializa la app y toods los modulos

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    api.add_resource(resources.UsuariosResources, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>', '/usuario')
    api.add_resource(resources.ConfiguracionResource, '/configuracion')
    api.add_resource(resources.LibrosResource, '/libros')
    api.add_resource(resources.LibroResource, '/libro/<id>', '/libro')
    api.add_resource(resources.PrestamosResource, '/prestamos')
    api.add_resource(resources.PrestamoResource, '/prestamo/<id>', '/prestamo')
    api.add_resource(resources.ValoracionesResource, '/valoraciones')
    api.add_resource(resources.ValoracionResource, '/valoracion/<id>', '/valoracion')
    api.add_resource(resources.LoginResource, '/login')
    api.add_resource(resources.NotificacionesResource, '/notificaciones')

    api.init_app(app)
    
    return app
