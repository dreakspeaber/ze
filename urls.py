from django.urls import path, include, re_path
from web import views

urlpatterns = [
    path('', views.home.as_view(),name='home'),
    path('login', views.signin.as_view()),
    path('logout', views.logoutpg.as_view()),


#add routes
    path('addcall', views.addCall.as_view()),
    path('addcontact', views.addContact.as_view()),
    path('addlogo', views.addlogo.as_view()),
    path('addhome', views.addhome.as_view()),
    path('addintro', views.addintro.as_view()),
    path('addgal', views.addgallery.as_view()),
    path('addproduct', views.addproduct.as_view()),
    path('addmethod', views.addmethod.as_view()),
    path('addlink', views.addlink.as_view()),
    path('<int:id>/addteam', views.addemployee.as_view(),name="addteam"),


#dashboard

    path('dash', views.dash.as_view(),name="dash"),
    path('dgal', views.dgal.as_view()),
    path('dcall', views.dcallme.as_view()),
    path('dfront', views.dfront.as_view()),
    path('<int:id>/dteam', views.dteam.as_view(),name="dteam"),




#delete

    path('<int:id>/deleteContact', views.deleteContact.as_view()),
    path('<int:id>/deletecall', views.deleteCall.as_view()),
    path('<int:id>/deletegal', views.deletegal.as_view()),
   path('<int:id>/deleteteam', views.deleteteam.as_view()),


]