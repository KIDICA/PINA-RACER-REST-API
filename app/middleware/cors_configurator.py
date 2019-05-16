
class CorsConfigurator(object):
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.set_header("Access-Control-Allow-Methods", "*")
        resp.set_header("Access-Control-Allow-Credentials", "*")
        resp.set_header("Access-Control-Allow-Headers", "*")
