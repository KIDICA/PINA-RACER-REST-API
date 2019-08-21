import falcon

from app.services.shield_service import ShieldService


class MotorResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        speed = int(req.get_param('speed', required=True))
        direction = int(req.get_param('direction', required=True))
        if speed < 300 or speed > 1000:
            resp.status = falcon.HTTP_400
            return

        if direction not in [0, 1]:
            resp.status = falcon.HTTP_400
            return

        self.shield_service.set_motor_speed(speed, direction)

        resp.status = falcon.HTTP_202
