import falcon

from app.services.shield_service import ShieldService


class LightResource(object):
    shield_service = ShieldService()

    def on_put(self, req, resp):
        red = int(req.get_param('red', default=0))
        green = int(req.get_param('green', default=0))
        blue = int(req.get_param('blue', default=0))

        self.shield_service.set_rgb_light(red, green, blue)

        resp.status = falcon.HTTP_200
