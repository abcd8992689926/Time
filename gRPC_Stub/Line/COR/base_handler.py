from models.handler.response import Response


class BaseHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, event) -> Response:
        if self.successor:
            return self.successor.handle_request(event)
