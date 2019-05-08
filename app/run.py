import falcon
from app.resources.images import ImageResource
from app.resources.root import RootResources

api = application = falcon.API()

root = RootResources()
images = ImageResource()

api.add_route('/', root)
api.add_route('/images', images)
