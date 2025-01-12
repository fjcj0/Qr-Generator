from rest_framework import serializers
class ConfigSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=255, allow_blank=True)
    eye = serializers.CharField(max_length=255, allow_blank=True)
    eyeBall = serializers.CharField(max_length=255, allow_blank=True)
    bodyColor = serializers.CharField(max_length=20, allow_blank=True)
    bgColor = serializers.CharField(max_length=20, allow_blank=True)
    eyeColor = serializers.CharField(max_length=20, allow_blank=True)  
    eyeBallColor = serializers.CharField(max_length=20, allow_blank=True)  
    gradientColor1 = serializers.CharField(max_length=20, allow_blank=True)
    gradientColor2 = serializers.CharField(max_length=20, allow_blank=True)
    gradientType = serializers.CharField(max_length=255, allow_blank=True)
    gradientOnEyes = serializers.BooleanField()
    logo = serializers.CharField(max_length=255, required=False, allow_blank=True)
    level = serializers.CharField(max_length=255, allow_blank=True)
class QrSerializer(serializers.Serializer):
    data = serializers.URLField()
    config = ConfigSerializer()
    size = serializers.IntegerField()
    download = serializers.BooleanField()
    file = serializers.CharField(max_length=20)
class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=40)
    email = serializers.EmailField(max_length=50)
class TokenSerializers(serializers.Serializer):
    token = serializers.CharField(max_length=300)
class QrUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    qr_code = serializers.CharField(max_length=300)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    downloaded_at = serializers.DateTimeField(required=False)
    description = serializers.CharField(max_length=250,allow_null=True)
    link = serializers.CharField(max_length=300,allow_null=True)
class ConfirmationSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=4)
    email = serializers.EmailField(max_length=255)
class UserDuplicateSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)