from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def heroes_list(request):
    return Response ('Father you are my foundation!')
