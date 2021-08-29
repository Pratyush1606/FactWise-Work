from django.urls.base import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from enterprise.models import * 
from enterprise.serializers import *


class user_permission(APIView):
    # Using an Authenticated Login
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            # Getting the user_id from user_auth
            user_id = UserAuth.objects.get(username=request.user).user_id_id
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # Checking if the user exists or not or is deleted
        user_check = User.objects.filter(user_id=user_id, deleted_datetime__isnull=True).exists()
        if(not user_check):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user_entity_relationship_id_list = UserEntity.objects.filter(user_id=user_id).values_list("user_entity_relationship_id", flat=True)
        user_permissions = UserPermission.objects.filter(user_entity_relationship_id__in=user_entity_relationship_id_list)
        data_to_return = []
        for user_permission in user_permissions:
            permissions = dict(UserPermissionSerializer(user_permission).data)
            permissions["entity_id"] = user_permission.get_entity_id()
            data_to_return.append(permissions)

        '''
        data_to_return = [
            {
                user_entity_relationship_id: 1,
                action_api_group: "abc",
                entity_id: 1
            },
        ]
        '''
        return Response(data=data_to_return, status=status.HTTP_200_OK)
    
    def post(self, request, entity_id):
        try:
            # Getting the user_id from user_auth
            user_id = UserAuth.objects.get(username=request.user).user_id_id
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Checking if the user exists or not or is deleted
        user_check = User.objects.filter(user_id=user_id, deleted_datetime__isnull=True).exists()
        if(not user_check):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user_entity = UserEntity.objects.get(entity_id=entity_id, user_id=user_id, deleted_datetime__isnull=True)
        except UserEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data["user_entity_relationship_id"] = user_entity.user_entity_relationship_id
        serializer = UserPermissionSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)