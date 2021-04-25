from django.http import JsonResponse


def fresh(request):
    return JsonResponse({"fresh": False})
