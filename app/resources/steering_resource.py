import falcon

from app.services.shield_service import ShieldService


class SteeringResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        value = int(req.get_param("value", required=True))
        if value < 40 or value > 140:
            resp.status = falcon.HTTP_400
            return

        self.shield_service.set_steering_direction(value)

        resp.status = falcon.HTTP_202
