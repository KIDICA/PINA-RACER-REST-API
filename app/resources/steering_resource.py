import falcon

from app.services.shield_service import ShieldService


class SteeringResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        payload = req.context["doc"]
        value = int(payload['value'])

        self.shield_service.set_steering_direction(value)

        resp.status = falcon.HTTP_202
