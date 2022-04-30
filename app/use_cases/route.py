import json
from request_objects.route import RouteRequest
from rest_framework.serializers import ValidationError
from repository.redis.redis import RedisRepo
from django.conf import settings

class AddJobUseCase:
    def __init__(
        self,
        redis_repo: RedisRepo
    ):
        self.__redis_repo = redis_repo

    def execute(self, route_request: RouteRequest):
        key_name= "full_jobs"
         
        res_repo = self.__redis_repo.save_job(route_request, key_name)

        if res_repo:
            return res_repo
        else:
            raise ValidationError({"message": 'Error in add job usecase'})

class GetJobUseCase:
    def __init__(
        self,
        redis_repo: RedisRepo
    ):
        self.__redis_repo = redis_repo

    def execute(self, status: str): 
        res_repo = self.__redis_repo.get_job("full_jobs")
        filtered_list = []
        response=None

        if status=="all":
            response = json.loads(res_repo) 
        else:    
            for i in json.loads(res_repo):
                if i["status"] == status:
                    filtered_list.append(i)
            response = filtered_list
        
        if response is not None:        
            return response
        else:
            raise ValidationError({"message": 'Error in get job usecase'})

class ProcessJobUseCase:
    def __init__(
        self,
        redis_repo: RedisRepo
    ):
        self.__redis_repo = redis_repo
        self.X = int(settings.X) #env variable, 10 seconds by default

    def execute(self): 
        res_repo = self.__redis_repo.get_job("full_jobs")
        processed_list = []
        response=None
 
        #while X-datetime.now()
        for job in json.loads(res_repo):
            if job["status"] != "processed":
                    processed_list.append(job)
            else:
                    current_data = job["data"]
                    new_data = []
                    addition = sum(current_data)
                    for d in current_data:
                        element = d + addition
                        new_data.append(element)

                    job["data"] = new_data
                    job["status"] = "processed"
                    processed_list.append(job)

        response = processed_list       
        
        if response is not None:        
            return response
        else:
            raise ValidationError({"message": 'Error in job processing usecase'})