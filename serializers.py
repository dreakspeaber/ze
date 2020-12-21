from rest_framework import serializers
from web.models import *

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model=Callme
        fields='__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logo
        fields='__all__'


class TmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tm
        fields='__all__'


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Intro
        fields='__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields='__all__'


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Methodology
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields='__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'



class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Links
        fields='__all__'
