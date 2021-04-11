from flask import Flask, request, redirect, render_template, url_for
from flask_restful import Resource, Api

# Importamos CORS
from flask_cors import CORS

# Import Resources
from resources.wellcome import Wellcome
from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from resources.items import Items
from resources.quality import Quality
from resources.sellin import Sellin

# Import from Repository the db_connection.py
from repository import db_connection


app = Flask(__name__)

CORS(app)

if app.config["ENV"] == "production":
    #Configuration APP Flask Production
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    #Configuration APP Flask Testing
    app.config.from_object("config.TestingConfig")
else:
    #Configuration APP Flask Development
    app.config.from_object("config.DevelopmentConfig")

# Init the Flask APP
db_connection.init_app(app)

#API REST to be able to test
api = Api(app, catch_all_404s=True)

# Add Resources
api.add_resource(Wellcome, '/')
api.add_resource(Inventario, '/inventory')
# GET item by name: '/items/name/<string:item_name>'
# POST, DELETE: '/items'
api.add_resource(Items, '/items/name/<string:item_name>', '/items', '/items/id/<int:id_item>/')
api.add_resource(Sellin, '/items/sellin/<int:item_sell_in>')
api.add_resource(Quality, '/items/quality/<int:item_quality>')
api.add_resource(UpdateQuality, '/update_quality')


#***********************************************************************

#***********************************************************************

#* APP ROUTES
# ******************************************
#* RUTE REDIRECCIONAR
@app.route('/')
def redireccionar():

    """
    RUTA REDIRECCIONAR A LA RUTA HOME
    """

    return redirect(url_for('login'))

# ******************************************

# ******************************************
#* RUTE HOME
@app.route('/login')
def home():

    """
    RUTA HOME
    """

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)