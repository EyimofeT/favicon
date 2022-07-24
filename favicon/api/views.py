import re
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from .models import User
# Create your views here.
import json

@api_view(['GET'])
def apiOverview(request):
    list={
        "User SignUp":"/signup/",
        "User LogIn":'/login/',
        "User Update":"/user-update/<str:pk>",
        "Users List":'/user-list/',
        "User Search":"/user-search/<str:pk>",
        "User Delete":"/user-delete/<str:pk>",
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
        # print(str(request.data['username']))
        request.data['username']=request.data['username'].lower()
        request.data['email']=request.data['email'].lower()
        serializer = UserSerializer(data=request.data)
        
        uname=str(request.data['username'])
        email=str(request.data['email'])
        uniqueUsernameStatus=checkUsernameInput(uname)
        uniqueEmailStatus=checkEmailInput(email)
        # print(uniqueUsernameStatus)
        # print(uniqueEmailStatus)
        if uniqueUsernameStatus==True and uniqueEmailStatus==True:
            
            # print(serializer.data["username"])
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
    # body= request.body
    # data={}
    # data = json.loads(body)
    # users = User.objects.get( =pk)
    # user_serializer = UserSerializer(users,many=False)
    # response=serializer.data
  
    username_input = request.data['username']
    try:
        users = User.objects.get(username=username_input)
        serializer = UserLoginSerializer(instance=users,data=request.data)
        user_serializer = UserSerializer(users,many=False)
        if serializer.is_valid():  
            # print(serializer.data['username'])
            if request.data['username']==serializer.data['username'] and request.data['password']==serializer.data['password']:
                
                user_cred=user_serializer.data
                user_cred.update({'User Key':'equishbkfoisdvniuwbvkwjnboqiua1234567u8io9pMofiiWroteThis'})
                user_cred.update({'Login Status':'Successful'})
                # response = {"User Login Successful" }
                response=user_cred
            else:
                response = {"Invalid Password"}     
        else:
            response = {
            "Check Credentials"
            }
    except:
        response = { 
            "Invalid Username"
        }
   
    return Response(response)

