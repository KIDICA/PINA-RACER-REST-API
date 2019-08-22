import json
import falcon

from app.services.shield_service import ShieldService


class SonicResource(object):
    shield_service = ShieldService()

    def on_get(self, req, resp):
        sonic = self.shield_service.get_sonic()
        echo_time = self.shield_service.get_sonic_echo_time()

        doc = {
            "sonic": sonic,
            "echoTime": echo_time
        }

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        value = int(req.get_param("value", required=True))
        print(value)
        if value < 0 or value > 360:
            resp.status = falcon.HTTP_400
            return

        self.shield_service.set_test_sonic_direction(value)

        resp.status = falcon.HTTP_200
