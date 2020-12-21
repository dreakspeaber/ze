from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, request
from rest_framework.views import APIView  
from rest_framework import viewsets
from rest_framework import generics, permissions, pagination
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate,logout, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser
#views
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render,redirect 
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,ListView,DeleteView,UpdateView
from django.views import View
from django.contrib.auth.models import User


#general packages
import random,requests
import json
import math
from web.models import *
from web.forms import *
from web.serializers import *


class AdminOnlyMixin(object):
    def has_permissions(self):
        return self.request.user.is_authenticated

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect(reverse('home'))
        return super().dispatch(
            request, *args, **kwargs)



class home(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request):
        intro = Intro.objects.get(pk=1)
        home = Home.objects.get(pk=1)
        logo = Logo.objects.get(pk=1)
        tm = Tm.objects.get(pk=1)
        method = Methodology.objects.get(pk=1)
        product = Product.objects.get(pk=1)
        gal = Gallery.objects.all().order_by('-id')
        employee = Employee.objects.all()
        link = Links.objects.get(pk=1)
        context = {
            'intro' : intro,
            'home' : home,
            'logo' : logo,
            'tm'   : tm,
            'method' : method,
            'product' : product,
            'gal' : gal,
            'employee' : employee,
            'link'  : link
        }
        return render(request,'web/index.html',context=context)



class signin(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request):
        if not request.user.is_anonymous:
            return redirect(reverse('dash'))
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request,'web/login.html',context=context)

    def post(self,request):
        user = authenticate(username=request.POST['name'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return Response({'status' : 'success'})


class logoutpg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))




class test(APIView):
    def get(self,request):
        intro = Intro.objects.get(pk=1)
        response = {
            'path' : intro.image.url
        }
        return Response(response)




#dashboard

class dash(AdminOnlyMixin,ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/contact.html'
    paginate_by=10

    
    def get_queryset(self):
        return Contact.objects.all().order_by('-id')


class dcallme(AdminOnlyMixin,ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/callme.html'
    paginate_by=10

    
    def get_queryset(self):
        return Callme.objects.all().order_by('-id')


class dfront(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request):
        intro = Intro.objects.get(pk=1)
        iform = IntroForm(instance=intro)
        home = Home.objects.get(pk=1)
        hform = HomeForm(instance=home)
        method = Methodology.objects.get(pk=1)
        mform = MethodForm(instance=method)
        product = Product.objects.get(pk=1)
        pform = ProductForm(instance=product)
        link = Links.objects.get(pk=1)
        lform = LinkForm(instance=link)
        context = {
            'intro' : intro,
            'home' : home,
            'method' : method,
            'product' : product,
            'hform' : hform,
            'iform' : iform,
            'mform' : mform,
            'pform' : pform,
            'lform' : lform
        }
        return render(request,'web/frontend.html',context=context)



class dgal(AdminOnlyMixin,ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/gallery.html'
    paginate_by=9

    def get_queryset(self):
        return Gallery.objects.all().order_by('-id')


class dteam(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request,*args,**kwargs):
        teams = Employee.objects.all()
        if self.kwargs['id']==0:
            form = TeamForm()
            id=0
        else:
            team = Employee.objects.get(pk=self.kwargs['id'])
            form = TeamForm(instance = team)
            id=self.kwargs['id']
        context = {

            'teams' : teams,
            'mform' : form,
            'tid'    : id
        }
        return render(request,'web/team.html',context=context)




#post routes

class addCall(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addContact(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addgallery(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#update post
class addintro(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        obj=Intro.objects.get(pk=1)
        serializer = IntroSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addhome(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request, *args, **kwargs):
        obj=Home.objects.get(pk=1)
        serializer = HomeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addmethod(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        obj=Methodology.objects.get(pk=1)
        serializer = MethodSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addtm(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request, *args, **kwargs):
        obj=Tm.objects.get(pk=1)
        serializer = TmSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addlogo(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request, *args, **kwargs):
        obj=Logo.objects.get(pk=1)
        serializer = LogoSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addproduct(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        obj=Product.objects.get(pk=1)
        serializer = ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addlink(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        obj=Links.objects.get(pk=1)
        serializer = LinkSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class addemployee(AdminOnlyMixin,APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def post(self,request, *args, **kwargs):
        if(self.kwargs['id']==0):
            serializer = TeamSerializer(data=request.data)
        else:
            obj=Employee.objects.get(pk=self.kwargs['id'])
            serializer = TeamSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#delete routes


class deleteContact(AdminOnlyMixin,APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        try:
            cat=Contact.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})



class deleteCall(AdminOnlyMixin,APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        try:
            cat=Callme.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})


class deletegal(AdminOnlyMixin,APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        try:
            cat=Gallery.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})



class deleteteam(AdminOnlyMixin,APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        try:
            cat=Employee.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})
