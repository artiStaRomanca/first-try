from django.shortcuts import render
from rest_framework import generics
from portofolio.models import StarTest, Category, Tag
from .serializers import StarTestSerializer
from rest_framework.response import Response
from rest_framework import status



class StarTestView(generics.ListCreateAPIView):
    queryset = StarTest.objects.all()
    serializer_class = StarTestSerializer

    def create(self, request):
        category_name = request.data['category']
        tags_names = request.data['tags']

        if category_name:
            try:
                Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                Category.objects.create(name=category_name)
        
        for tag in tags_names:
            try:
                Tag.objects.get(caption=tag)
            except Tag.DoesNotExist:
                Tag.objects.create(caption=tag)
            

        serializer = StarTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data":serializer.data
            }) 
        else:
            return Response({
                "errors":serializer.errors
            })

    # def create(self, request, *args, **kwargs):
    #     category_name =  request.POST.get('category', None)
    #     data = {
    #         "title": request.POST.get('title'),
    #         "category": "Puzzle",
    #         }
    #     _serializer = self.serializer_class(data=data) 
    #     if _serializer.is_valid():
    #         _serializer.save()
    #         return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
    #     else:
    #         return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA
