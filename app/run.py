import falcon

from app.middleware import RequestValidator, CorsConfigurator
from app.models.http_error import error_handler
from app.resources.motor_resource import MotorResource
from app.resources.root import RootResources
from app.resources.steering_resource import SteeringResource
from app.resources.sonic_resource import SonicResource

root = RootResources()
motor = MotorResource()
steering = SteeringResource()
sonic = SonicResource()

api = application = falcon.API(
    independent_middleware=False,
    middleware=[
        CorsConfigurator(),
        RequestValidator()
    ]
)

api.add_error_handler(Exception, error_handler)

api.add_route('/', root)
api.add_route('/motor', motor)
api.add_route('/steering', steering)
api.add_route('/sonic', sonic)
