import json
import stringcase
from jsonschema import validate, ValidationError, SchemaError

from app.models.schemas import JsonSchemas

from app.models.http_error import HttpError


class RequestValidator(object):

    def process_request(self, req, resp):
        if (req.content_length in (None, 0)) or (req.method == "OPTIONS"):
            return

        body = req.stream.read()
        if not body:
            raise HttpError(400, "A valid JSON document is required.")

        try:
            req.context["doc"] = json.loads(body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError):
            raise HttpError(400, "JSON was incorrect")

    def process_resource(self, req, resp, resource, params):
        if req.method == "OPTIONS":
            return
        name = [resource.__class__.__name__, stringcase.lowercase(getattr(req, "method", None)), "request schema"]
        schema = getattr(JsonSchemas, stringcase.snakecase(" ".join(name)), None)
        payload = req.context["doc"]

        if schema is not None:
            try:
                validate(payload, schema)
            except ValidationError:
                raise HttpError(400, "JSON is invalid")
            except SchemaError:
                raise HttpError(500, "Unable to check the request because the JSON scheme is invalid.")

    def process_response(self, req, resp, resource, req_succeeded):
        if "doc" not in req.context:
            return

        resp.body = json.dumps(req.context["result"])
