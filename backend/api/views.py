import json
from django.http import JsonResponse


def api_home(request):
    # request -> HttpRequest
    body = request.body  # Byte String of JSON data
    data = {}
    try:
        data = json.loads(body)  # String of JSON data  -> Python dictionary
    except:
        pass
    print(data.keys())
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    data["params"] = request.GET
    return JsonResponse(data)
