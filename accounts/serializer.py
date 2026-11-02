from rest_framework import serializers

from accounts.models import User

class Userserializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields= ["username","email","password","phone"]

        read_only_fields = ["id"]