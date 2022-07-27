from urllib import response
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from .models import ImageUpload

from api.models import User
from api.serializers import UserSerializer
from .serializers import ImageUploadSerializer
# Create your views here.




@api_view(['GET'])
def imgOverview(request):
    list={
        "Upload Image":"/img/upload/",
    }
    return Response(list)

@api_view(['POST'])
def imgUpload(request):
    token= request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try:
        
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
    
    user = User.objects.filter(id=payload['id']).first()
    # user = User.objects.get(id=payload['id'])
    serializer= UserSerializer(user)
    
    #adding user id from token
    request.data.update({'user_id' : serializer.data['id']})
    
    #calling the imageupload serializer
    imageserializer = ImageUploadSerializer(data=request.data)
    
    if imageserializer.is_valid():
        imageserializer.save()
        response = {
            "Success": "Image Uploaded",
            "Status" : 200,
            "image":imageserializer.data,
        }
    else:
        response = imageserializer.errors 
    
    print(imageserializer.data)
    return Response(response)
    # return Response(token)
    #return Response({"Succes": "200"})
    