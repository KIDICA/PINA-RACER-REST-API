import falcon
from falcon_cors import CORS

from app.middleware.request_validator import RequestValidator
from app.models.http_error import error_handler
from app.resources.motor_resource import MotorResource
from app.resources.root import RootResources
from app.resources.steering_resource import SteeringResource

cors = CORS(allow_all_origins=True,
            allow_all_headers=True,
            allow_all_methods=True)

root = RootResources()
motor = MotorResource()
steering = SteeringResource()

api = application = falcon.API(
    independent_middleware=False,
    middleware=[
        cors.middleware,
        RequestValidator()
    ]
)

api.add_error_handler(Exception, error_handler)

api.add_route('/', root)
api.add_route('/motor', motor)
api.add_route('/steering', steering)
