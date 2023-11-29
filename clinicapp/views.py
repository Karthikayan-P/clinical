from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from .models import clinicuser
from .serializer import clinicregisterserializer
from .forms import clinicform
from rest_framework.generics import ListAPIView


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class CadminRegistrationView(generics.CreateAPIView):
    queryset = clinicuser.objects.all()
    serializer_class = clinicregisterserializer

    def create(self, request, *args, **kwargs):
        form = clinicform(request.data)
        if form.is_valid():
            user = self.perform_create(form)

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            response_data = {
                'token': token,
                'user_id': user.id,
                'username': user.username,
                'role': user.role,
            }

            return Response(response_data)
        else:
            return Response(form.errors, status=400)

    def perform_create(self, form):
        return form.save()