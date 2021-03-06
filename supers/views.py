from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from .models import Super
from .serializer import SuperSerializer
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':
        villains_heroes = SuperType.objects.all()
        custom_response_dictionary = {}
        heroes_and_villains = request.query_params.get('type')
        if heroes_and_villains:
                the_super = Super.objects.filter(super_type__super_type=heroes_and_villains)
                supers_serializer = SuperSerializer(the_super, many=True) 
                return Response(supers_serializer.data)
        
        for super in villains_heroes:
            heroes_villains = Super.objects.filter(super_type_id = super.id)
            supers_serializer = SuperSerializer(heroes_villains, many=True)
            custom_response_dictionary[super.super_type] = supers_serializer.data
        return Response (custom_response_dictionary)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def villains_heroes_by_id(request, pk):
        super = get_object_or_404(Super,pk=pk)
        if request.method == 'GET':
            serializer = SuperSerializer(super)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializers = SuperSerializer(super, data = request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        elif request.method == "DELETE":
            super.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
