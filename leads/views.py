from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from leads.serializers import LeadSerializer
from leads.models import Lead
from leads.permissions import IsOwner

class LeadListView(ListAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LeadSerializer

    def list(self, request):

        leads = Lead.objects.filter(created_by=request.user)

        serializer = LeadSerializer(leads, many=True)

        return Response(serializer.data)

class LeadCreateView(CreateAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):

        form_data = request.data

        serializer = LeadSerializer(data = form_data)

        if serializer.is_valid():

            serializer.save(created_by=request.user)

            return Response(data=serializer.data)

        else:

            return Response(data=serializer.errors)


class LeadRetrieveViewUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated, IsOwner]

    serializer_class = LeadSerializer

    queryset = Lead.objects.all()


