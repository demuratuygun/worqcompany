from rest_framework import serializers
from .models import User, Platform
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("isim sadece harf ve bosluklardan olusabilir")
        return value

    def validate_surname(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("soyisim sadece harflerden olusabilir")
        return value

    def validate_email(self, value):
        # regular expression for validating an Email 
        valid_email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not re.fullmatch(valid_email_regex, value):
            raise serializers.ValidationError("lutfen gecerli bir eposta girin")
        return value
    
    def validate_phone(self, value):
        if not value.replace(" ", "").isnumeric():
            raise serializers.ValidationError("lutfen gecerli bir telefon numarasi girin")
        return value


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

    def validate_url(self, value):
        # regular expression for validating an Email 
        valid_url_regex = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

        if not re.fullmatch(valid_url_regex, value):
            raise serializers.ValidationError("lutfen gecerli bir url girin")
        return value
    
    def validate_platform(self, value):
        if value!="Trendyol" and value!="Hepsiburada" and value!="Amazon":
            raise serializers.ValidationError("lutfen gecerli bir platform secin")
        return value
        
