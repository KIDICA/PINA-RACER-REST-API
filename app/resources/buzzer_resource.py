import falcon

from app.services.shield_service import ShieldService


class BuzzerResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        value = int(req.get_param("value", required=True))
        if value < 0 or value > 2000:
            resp.status = falcon.HTTP_400
            return

        self.shield_service.set_buzzer_volume(value)

        resp.status = falcon.HTTP_200
