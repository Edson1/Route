from rest_framework.views import APIView
from rest_framework.request import Request
from http_response.http_response import HttpResponse

from backend_authentication import Authentication
from use_cases.route import AddJobUseCase, GetJobUseCase
from repository.redis.redis import RedisRepo
from request_objects.route import RouteRequest

class RouteView(APIView):
    authentication_classes = (Authentication,)
    permission_classes=[]
    http_response = HttpResponse()

    def get(self, request: Request):
        redis_repo = RedisRepo() 
        uc = GetJobUseCase(redis_repo) 

        if(request.query_params.get('status') is not None):
            response = uc.execute(request.query_params.get('status'))
        else:       
            response = uc.execute("all")

        if(response):
            return HttpResponse.Success(response)
 
        return HttpResponse.ServerError("Empty Response") 

    def post(self, request: Request):
        #RequestSerializer(data=request.data).is_valid(raise_exception=True)
        redis_repo = RedisRepo() 
        uc = AddJobUseCase(redis_repo)

        route_request = RouteRequest.from_dict(request.data)
        response = uc.execute(route_request)

        if response is not None:
            return HttpResponse.Success(response)

        return HttpResponse.ServerError(response)