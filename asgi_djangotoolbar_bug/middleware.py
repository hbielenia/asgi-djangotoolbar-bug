from django.core.exceptions import MiddlewareNotUsed


class DummyMiddleware:

    def __init__(self, get_response):
        raise MiddlewareNotUsed
