from rest_framework import serializers

# Token
class LoginSocialSerializer(serializers.Serializer):
    
    token_id = serializers.CharField(required=True)
    