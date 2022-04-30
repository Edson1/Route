run in localhost 8000 from app folder:
python .\manage.py runserver

Add HTTP Authorization header:
    Bearer Token: "allow"

## POST /route/
body:
{
    "name": "My Job 1",
    "data": [1, 2, 3]
}

return OK 200: 
[
    {
        "name": "My Job 1",
        "id": 1,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    }
]

## GET /route/?status=pending
filter by status
return OK 200: 
[
    {
        "name": "My Job 1",
        "id": 1,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    },
    {
        "name": "My Job 2",
        "id": 2,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    },
    {
        "name": "My Job 3",
        "id": 3,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    }
]

## GET /route/
All jobs:
return OK 200: 
[
    {
        "name": "My Job 1",
        "id": 1,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    },
    {
        "name": "My Job 2",
        "id": 2,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    },
    {
        "name": "My Job 3",
        "id": 3,
        "status": "pending",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    },
    {
        "name": "My Job 4",
        "id": 4,
        "status": "other",
        "data": [
            1,
            2,
            3
        ],
        "result": "something"
    }
]