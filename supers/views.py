from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from .models import Super
from .serializer import SuperSerializer



@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':
        villians_heroes = SuperType.objects.all()
        custom_response_dictionary = {}
        for super_type in villians_heroes:
            heroes_villians = Super.objects.filter(super_type_id = super_type.id)
            supers_serializer = SuperSerializer(heroes_villians, many=True)
            custom_response_dictionary[super_type.super_type] = supers_serializer.data
        return Response (custom_response_dictionary)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



