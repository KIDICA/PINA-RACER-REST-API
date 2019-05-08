import falcon
from falcon_cors import CORS
from app.resources.motor import MotorResource
from app.resources.root import RootResources

cors = CORS(allow_origins_list=['http://localhost:4200'])

root = RootResources()
images = MotorResource()

api = application = falcon.API(middleware=[cors.middleware])
public_cors = CORS(allow_all_origins=True)

api.add_route('/', root)
api.add_route('/motor', images)
