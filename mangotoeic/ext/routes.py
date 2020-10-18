from mangotoeic.legacy.api import Legacy, Legacyes
from mangotoeic.newq.api import NewQ, NewQs
from mangotoeic.corpus.api import Corpus, Corpuses
from mangotoeic.home.api import Home

def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(Legacy, '/api/legacy/<string:id>')
    api.add_resource(Legacyes,'/api/legacyes')
    api.add_resource(NewQ, '/api/newq/<string:id>')
    api.add_resource(NewQs, '/api/newqs')
    api.add_resource(Corpus, '/api/corpus/<string:id>')
    api.add_resource(Corpuses, '/api/corpuses/')