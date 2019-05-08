import falcon
from falcon_cors import CORS
from app.resources.motor import MotorResource
from app.resources.root import RootResources

cors = CORS(allow_origins_list=['http://localhost:4200'])

root = RootResources()
motor = MotorResource()

api = application = falcon.API(middleware=[cors.middleware])

api.add_route('/', root)
api.add_route('/motor', motor)
