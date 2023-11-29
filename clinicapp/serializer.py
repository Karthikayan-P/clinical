from rest_framework import serializers
from .models import clinicuser
from .forms import clinicform

class clinicregisterserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = clinicuser
        fields = ('username', 'password', 'role')

    def create(self, validated_data):
        form = clinicform(validated_data)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(validated_data['password'])
            user.save()
            return user