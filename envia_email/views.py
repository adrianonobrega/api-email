from email import message
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config
from rest_framework.views import APIView, Response, status
from traitlets import Undefined
# Create your views here.


class EnviarEmail(APIView):

     def post(self,request):
        
        send_mail(config('SUBJECT'),str(request.data),config('EMAIL_HOST_USER'),[config('EMAIL_DESTINATION')])
        return Response("Email enviado com sucesso",200)




        

        