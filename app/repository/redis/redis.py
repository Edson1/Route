import json
import redis
from request_objects.route import RouteRequest
from django.conf import settings
from rest_framework.serializers import ValidationError

class RedisRepo:
    def __init__(self):
        self.__redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port='6380',
            password=settings.REDIS_PASSWORD,
            ssl=settings.REDIS_SSL,
            connection_pool=settings.REDIS_POOL
        )
    
    def save_job(self, route_request: RouteRequest, key_name: str):
        try:
            current_jobs = self.get_job(key_name)
            current_jobs = json.loads(current_jobs.decode("utf-8"))
            id = len(current_jobs)+1
        except Exception as ex:
            current_jobs = []
            id = 1
        
        new_job = {
            "name": route_request.name,
            "id": id,
            "status": "other",
            "data": route_request.data,
            "result": "something"
        }

        current_jobs.append(new_job)
        route_request_value = current_jobs

        if route_request:
            value = json.dumps(route_request_value)
            try:
                self.__redis_client.set(
                    key_name,
                    value
                )
                return route_request_value
            except Exception as ex:
                print(ex)
                raise ValidationError("Writing Error in cache repo: redis.set()")

    def get_job(self, key: str): 
        cache_data = self.__redis_client.get(key)
        if cache_data:
            print(cache_data)
            return cache_data 
        else: 
            raise ValidationError("Reading Error from cache repo, Not found record: "+ key)


