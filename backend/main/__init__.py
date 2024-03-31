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

    api.init_app(app)
    
    return app
