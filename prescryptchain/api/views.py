# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# REST
from rest_framework.viewsets import ViewSetMixin
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# our models
from blockchain.models import Block, Prescription, Medication

# Define router
router = routers.DefaultRouter()

class PrescriptionSerializer(serializers.ModelSerializer):
    """ Prescription serializer """
    class Meta:
        model = Prescription
        fields = (
            'id',
            'medic_name',
            'medic_cedula',
            'medic_hospital',
            'patient_name',
            'patient_age',
            'diagnosis',
            'location',
            'timestamp',
            'signature',
            'get_before_hash',
            'raw_size',
        )
        read_only_fields = ('id', 'timestamp', 'signature',)


class PrescriptionViewSet(viewsets.ModelViewSet):
    """ Prescription Viewset """
    serializer_class = PrescriptionSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Prescription.objects.all().order_by('-timestamp')


# add patient filter by email, after could modify with other
router.register(r'rx-endpoint', PrescriptionViewSet, 'prescription-endpoint')


class BlockSerializer(serializers.ModelSerializer):
    """ Prescription serializer """
    class Meta:
        model = Block
        fields = (
            'id',
            'hash_block',
            'get_before_hash',
            'raw_size',
            'data',
            'timestamp',
        )
        read_only_fields = ('id', 'hash_block','timestamp','get_before_hash', 'raw_size', 'data', )


class BlockViewSet(viewsets.ModelViewSet):
    """ Prescription Viewset """
    serializer_class = BlockSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Block.objects.all().order_by('-timestamp')


# add patient filter by email, after could modify with other
router.register(r'block', BlockViewSet, 'block-endpoint')
