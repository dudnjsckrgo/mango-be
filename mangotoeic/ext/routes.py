from mangotoeic.item.item_api import ItemApi
def initialize_routes(api):
    api.add_resource(ItemApi, '/api/item')