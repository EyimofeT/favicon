import re
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
import json
import jwt, datetime

@api_view(['GET'])
def apiOverview(request):
    list={
        "User SignUp":"/signup/",
        "User LogIn":'/login/',
        "User Update":"/user-update/<str:pk>",
        "Users List":'/user-list/',
        "User Search":"/user-search/<str:pk>",
        "User Delete":"/user-delete/<str:pk>",
        "logout":"/logout/",
        "User View" : "/user-view/"
    }
    return Response(list)

@api_view(['GET'])
def userList(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        response=serializer.data
    
    except:
        response = {
            "Error Occured"
        }
    return Response(response)

@api_view(['GET'])
def userSearch(request,pk):
    try:
        users = User.objects.get(id=pk)
        serializer = UserSerializer(users,many=False)
        response=serializer.data
    except:
        response = {
            "Error Occured"
        }
    return Response(response)

def checkUsernameInput(input_username):
    try: 
        username_check = User.objects.get(username=input_username)
        # username_serializer = UserSerializer(instance=username_check,many=False)
        # if username_serializer is not None:
        #     return False
        if username_check:
            return False
        
    except:
        # response= {"An Error Has Occured"}
            return True

def checkEmailInput(input_email):
    try:
            email_check = User.objects.get(email=input_email)
            # username_check = User.objects.get(username=uname)
            # email_serializer = UserSerializer(instance=email_check,many=False)
            # if email_serializer is not None:
            #     return False
            if email_check:
                return False
            # elif email_check==username_check:
            #     print("Here")
            #     return True
    except:
            return True


@api_view(['POST'])
def userCreate(request):
    try:
        # request.data['first_name']=request.data['first_name'].capitalize()
        # request.data['last_name']=request.data['last_name'].capitalize()
        request.data['username']=request.data['username'].lower()
        request.data['email']=request.data['email'].lower()
        
        serializer = UserSerializer(data=request.data)
        
        uname=str(request.data['username'])
        email=str(request.data['email'])
        uniqueUsernameStatus=checkUsernameInput(uname)
        uniqueEmailStatus=checkEmailInput(email)
        if uniqueUsernameStatus==True and uniqueEmailStatus==True:
             
            if serializer.is_valid():  
                serializer.save()
                response = {
                "User Create Successful"
                }
            else:
                response = {
                "Error: User Not Created : Check Input"
                }
        elif uniqueUsernameStatus==False and uniqueEmailStatus==True:
            response = {
                        "Error: Username Already Exists"
                        } 
        elif uniqueUsernameStatus==True and uniqueEmailStatus==False:
            response = {
                        "Error: Email Already Exists"
                        } 
        elif uniqueUsernameStatus==False and uniqueEmailStatus==False:
            response = {
                        "Error: Username and Email Already Exists"
                        }    
    
    except:
        response = {
            "Error Occured"
        }
    
    return Response(response)

@api_view(['POST'])
def userUpdate(request,pk):
    try:
        #check if user has been used and confirms it in lower case
        request.data['username']=request.data['username'].lower()
        request.data['email']=request.data['email'].lower()
        uname=str(request.data['username'])
        email=str(request.data['email'])
        
        # uniqueUsernameStatus=checkUsernameInput(uname)
        # uniqueEmailStatus=checkEmailInput(email)
        
        users = User.objects.get(id=pk)
        serializer = UserSerializer(instance=users,data=request.data)
        
        if serializer.is_valid():  
            serializer.save()
            response = {
            "User Update Successful"
            }
        else:
            response = {
            "Error: User Not Updated"
            }
        # if uniqueUsernameStatus==True and uniqueEmailStatus==True:
            
        #     # print(serializer.data["username"])
        #     if serializer.is_valid():  
        #         # serializer.save()
        #         response = {
        #         "User Update Successful"
        #         }
        #     else:
        #         response = {
        #         "Error: User Not Updated : Check Input"
        #         }
        # elif uniqueUsernameStatus==False and uniqueEmailStatus==True:
        #     response = {
        #                 "Error: Username Already Exists"
        #                 } 
        # elif uniqueUsernameStatus==True and uniqueEmailStatus==False:
        #     response = {
        #                 "Error: Email Already Exists"
        #                 } 
        # elif uniqueUsernameStatus==False and uniqueEmailStatus==False:
        #     response = {
        #                 "Error: Username and Email Already Exists"
        #                 }    
    except:
        response = {
            "Error Occured"
        }
    return Response(response)

@api_view(['POST'])
def userDelete(request,pk):
    try:
        user = User.objects.get(id=pk)
    
        if user:
            user.delete()    
            response = {
                "User Delete Successful"
            }
        else:
            response = {
                "Error: User Delete Unsuccessful"
            }
    except:
        response = {
            "Error Occured"
        }
    # serializer = UserSerializer(instance=users,data=request.data)
    
    # if serializer.is_valid():  
    #     serializer.save()
    #     response = {
    #         "User Updatee Successfully"
    #     }
    # else:
    #     response = {
    #         "Error: User Not Updated"
    #     }
    return Response(response)

@api_view(['POST'])
def userLogin(request):
    
    username_input = request.data['username']
    password_input = request.data['password']
    user=User.objects.filter(username=username_input).first()
    user_serializer = UserSerializer(user,many=False)
    
    if user is None:
        raise AuthenticationFailed("User not Found!")
    
    if not user.check_password(password_input):
        raise AuthenticationFailed("Incorrect Password!")
    
    payload = {
        'id':user.id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
        "is_superuser": user.is_superuser ,
        
    }
    token = jwt.encode(payload, 'secret',algorithm='HS256')
    # .decode('utf-8')
    
    response =Response()
    response.set_cookie(key='jwt', value=token,httponly=True)
    response.data= {
        "Message" : "Login Successful", 
        "Status":200,
        'jwt' : token
    }
   
    
    # return Response(user_serializer.data)
    return response
    
#     try:
#         users=User.objects.filter(username=username_input).first()
#         # users = User.objects.get(username=username_input)
#         serializer = UserLoginSerializer(instance=users,data=request.data)
#         user_serializer = UserSerializer(users,many=False)
#         if serializer.is_valid():  
#             # print(serializer.data['username'])
#             if request.data['username']==serializer.data['username'] and request.data['password']==serializer.data['password']:
                
#                 user_cred=user_serializer.data
#                 # user_cred.update({'User Key':'equishbkfoisdvniuwbvkwjnboqiua1234567u8io9pMofiiWroteThis'})
#                 # user_cred.update({'Login Status':'Successful'})
#                 # response = {"User Login Successful" }
#                 response=user_cred
#             else:
#                 response = {"Invalid Username/Password"}     
#         else:
#             response = {
#             "Check Input Values"
#             }
#     except:
#         response = { 
#             "Invalid Username/Password"
#         }
   
#     return Response(response)
@api_view(['GET'])
def userView(request):
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
    
    return Response(serializer.data)
    # return Response(token)

@api_view(['POST'])    
def logout(request):
    response=Response()
    response.delete_cookie('jwt')
    response.data={
        'Message': 'Logout Successful'
    }
    return response