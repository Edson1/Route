import dataclasses
from rest_framework.response import Response

@dataclasses.dataclass
class HttpResponse:

    @staticmethod
    def Success(data):
        return Response(
            status=200,
            data=data
        )

    @staticmethod
    def CustomError(status_code, message):
        return Response(
            status=status_code,
            data={
                'message': message
            }
        )
    
    @staticmethod
    def Created(data):
        return Response(
            status=201,
            data=data
        )
    
    @staticmethod
    def BadRequest(code, message):
        return Response(
            status=400,
            data={
                'code': code,
                'message': message
            }
        )
    
    @staticmethod
    def Unauthorized():
        return Response(
            status=401,
            data={
                'code': 'Unauthorized',
                'message': 'Unauthorized to access'
            }
        )
    
    @staticmethod
    def Forbiden():
        return Response(
            status=403,
            data={
                'code': 'Forbidden', 
                'message': 'Wrong password, token or API key'
            }
        )
    
    @staticmethod
    def ServerError(message):
        return Response(
            status=500,
            data={
                'error': 'Internal Server Error',
                'status': 500,
                'message': message
            }
        )

    

    