import falcon

import asyncio
import datetime
import random
import websockets

from app.services.shield_service import ShieldService

from app.middleware import CorsConfigurator
from app.models.http_error import error_handler
from app.resources.motor_resource import MotorResource
from app.resources.root import RootResources
from app.resources.steering_resource import SteeringResource
from app.resources.sonic_resource import SonicResource
from app.resources.buzzer_resource import BuzzerResource
from app.resources.light_resource import LightResource

shield = ShieldService()

root = RootResources()
motor = MotorResource()
steering = SteeringResource()
sonic = SonicResource()
buzzer = BuzzerResource()
light = LightResource()

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
api.add_route('/light', light)


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Ready
shield.set_rgb_light(0, 0, 1)


