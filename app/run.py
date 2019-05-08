import falcon
from app.resources.motor import MotorResource
from app.resources.root import RootResources
api = application = falcon.API()

root = RootResources()
images = MotorResource()

api.add_route('/', root)
api.add_route('/motor', images)
