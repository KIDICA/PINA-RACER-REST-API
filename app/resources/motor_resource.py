import falcon

from app.services.shield_service import ShieldService


class MotorResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        payload = req.stream.read()
        print(payload)
        speed = int(payload['speed'])
        direction = int(payload['direction'])

        self.shield_service.set_motor_speed(speed, direction)

        resp.status = falcon.HTTP_202
