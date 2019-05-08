import json
import falcon


class RootResources(object):
    def on_get(self, req, resp):
        doc = {
            "name": "pia-racer-rest-api",
            "version": "0.0.1"
        }

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
