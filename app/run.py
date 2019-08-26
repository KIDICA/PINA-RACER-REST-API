import falcon

from app.middleware import CorsConfigurator
from app.models.http_error import error_handler
from app.resources.motor_resource import MotorResource
from app.resources.root import RootResources
from app.resources.steering_resource import SteeringResource
from app.resources.sonic_resource import SonicResource
from app.resources.buzzer_resource import BuzzerResource

root = RootResources()
motor = MotorResource()
steering = SteeringResource()
sonic = SonicResource()
buzzer = BuzzerResource()

api = application = falcon.API(
    independent_middleware=False,
    middleware=[
        CorsConfigurator()
    ]
)

api.req_options.auto_parse_form_urlencoded = True

api.add_error_handler(Exception, error_handler)

api.add_route('/', root)
api.add_route('/motor', motor)
api.add_route('/steering', steering)
api.add_route('/sonic', sonic)
api.add_route('/buzzer', buzzer)
