from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

class Authentication(authentication.BaseAuthentication):
    keywords = ['Token', 'Bearer']
    model = None

    def authenticate(self, request):
        authorization = get_authorization_header(request).split()
        if len(authorization) == 0:
            raise exceptions.AuthenticationFailed("authorization header not provided")
        else:
            try:
                print(authorization)
                if not authorization[0].decode() in self.keywords:
                    msg = 'Invalid keywords header.'
                    raise exceptions.AuthenticationFailed(msg)
                if authorization[1].decode()=="allow":
                    response = ("request","allowed")
                else: raise exceptions.AuthenticationFailed({"error": "Unathorized to access this resource", "status": 403})
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        print(response)
        return response

