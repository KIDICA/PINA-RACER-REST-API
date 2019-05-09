import falcon
import logging
from falcon_cors import CORS

from app.middleware.request_validator import RequestValidator
from app.models.http_error import error_handler
from app.resources.motor_resource import MotorResource
from app.resources.root import RootResources

logger = logging.getLogger(__name__)

cors = CORS(allow_origins_list=['http://localhost:4200'],
            allow_all_methods=True)

root = RootResources()
motor = MotorResource()

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
