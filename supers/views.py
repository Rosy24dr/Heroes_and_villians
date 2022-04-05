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


@api_view(['GET','PUT', 'DELETE'])
def villians_heroes_by_id(request, pk):
    try:
        super = Super.objects.get(pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Super.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    
    return Response(pk)

    #  car = get_object_or_404(Car, pk=pk)
    #  if request.method == 'GET': 
    #     serializers = CarSerializer(car);
    #     return Response(serializers.data)
    #  elif request.method == 'PUT':
    #     serializers = CarSerializer(car, data = request.data)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response(serializers.data)
    #  elif request.method == "DELETE":
    #      car.delete()
    #      return Response(status = status.HTTP_204_NO_CONTENT)
