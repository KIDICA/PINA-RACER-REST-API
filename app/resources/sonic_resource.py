import falcon

from app.services.shield_service import ShieldService


class SonicResource(object):
    shield_service = ShieldService()

    def on_get(self, req, resp):
        resp.body = "Test"
