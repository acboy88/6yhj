from django.utils.deprecation import MiddlewareMixin

class HttpResponseCustomHeader(MiddlewareMixin):
    def process_response(self, request, response):
        response["Referrer-Policy"] = "unsafe-url"
        if not response.has_header("Product"):
            response["Product"] = "lekuwang 1.1"
        return response
