
from flask import Flask
from flask_restful import Api
from mangotoeic.ext.db import url, db
from mangotoeic.ext.routes import initialize_routes
from mangotoeic.corpus.api import Corpus, Corpuses
from mangotoeic.legacy.api import Legacy, Legacyes
from mangotoeic.newq.api import NewQ, NewQs


app = Flask(__name__)
print('========== url ==========')
print(url)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

initialize_routes(api)

with app.app_context():
    db.create_all()