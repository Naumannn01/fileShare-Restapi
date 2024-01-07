from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser
def core(request):
    return render(request,'home.html')

def download(request, uid):
    return render(request, 'download.html',context={'uid':uid})

class HandleFileUpload(APIView):
    def post(self,request):
        try:
            data=request.data
            serailizer=FileListSerializer(data=data)
            if serializer.is_valid():
                serailizer.save()
                return Response({
                    'status':200,
                    'message':'Files uploaded successfully',
                    'data':searializer.data
                })
            return Response({
                    'status':400,
                    'message':'Something went wrong',
                    'data':searializer.errors
                })
        except Exception as e:
            print(e)