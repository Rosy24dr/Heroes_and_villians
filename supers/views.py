from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializer import SuperSerializer


@api_view(['GET'])
def super_list(request):

    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response (serializer.data, status = status.HTTP_200_OK)


# @api_view(['GET'])
# def super_typerequest):
#     supers = Super.objects.all()
#     serializer = SuperSerializer(supers, many=True)
#     return Response (serializer.data)

# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import CarSerializer
# from .models import Car
# from cars import serializers

# @api_view(['GET', 'POST'])
# def cars_list(request):

#     if request.method == 'GET':
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data, status = status.HTTP_201_CREATED)
   

# @api_view(['GET','PUT', 'DELETE'])
# def car_detail(request, pk):
#      car = get_object_or_404(Car, pk=pk)
#      if request.method == 'GET': 
#         serializers = CarSerializer(car);
#         return Response(serializers.data)
#      elif request.method == 'PUT':
#         serializers = CarSerializer(car, data = request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)
#      elif request.method == "DELETE":
#          car.delete()
#          return Response(status = status.HTTP_204_NO_CONTENT)

