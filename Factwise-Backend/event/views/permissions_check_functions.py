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
from event.models import * 
from event.serializers import *

def event_criteria_matches(event_info, criteria):
    '''
    Function for checking the criteria related to an event, taking event_info model and criteria as string
    '''
    if(criteria==""):
        return True

    # Rest logic will be implemented further
    return False

def event_permission_check(event_id, user_id, allowed_action_group_list, entity_id):
    try:
        event_info = Event.objects.get(event_id=event_id)
    except Event.DoesNotExist:
        return False

    try:
        user_entity = UserEntity.objects.get(user_id=user_id, entity_id=entity_id, deleted_datetime__isnull=True)
    except UserEntity.DoesNotExist:
        return False

    # Getting all user permissions for this user and entity
    applicable_user_permissions_list = UserPermission.objects.filter(user_entity_relationship_id=user_entity.user_entity_relationship_id, action_api_group__in=allowed_action_group_list)
    
    for user_permission in applicable_user_permissions_list:
        if(event_criteria_matches(event_info, user_permission.criteria)):
            # If this user_id is under the event special permission list
            event_permission_restricted_list = EventPermission.objects.filter(event_id=event_id, action_api_group=user_permission.action_api_group)
            if(not event_permission_restricted_list):
                return True

            event_permission_restricted_list_user_check = event_permission_restricted_list.filter(user_id=user_id).exists()
            if(event_permission_restricted_list_user_check):
                return True
    return False

def draft_event_permission_check(event_id, user_id, allowed_action_group_list, entity_id):
    try:
        event_info = DraftEvent.objects.get(event_id=event_id)
    except Event.DoesNotExist:
        return False

    try:
        user_entity = UserEntity.objects.get(user_id=user_id, entity_id=entity_id, deleted_datetime__isnull=True)
    except UserEntity.DoesNotExist:
        return False

    # Getting all user permissions for this user and entity
    applicable_user_permissions_list = UserPermission.objects.filter(user_entity_relationship_id=user_entity.user_entity_relationship_id, action_api_group__in=allowed_action_group_list)
    
    # Remove this check if below extra checks are being implemented
    if(len(applicable_user_permissions_list)>0):
        return True
    
    # If some extra checks have to implemented below for draft event, above if check should be removed

    # for user_permission in applicable_user_permissions_list:
    #     if(event_criteria_matches(event_info, user_permission.criteria)):
    #         # If this user_id is under the event special permission list
    #         event_permission_restricted_list = EventPermission.objects.filter(event_id=event_id, action_api_group=user_permission.action_api_group)
    #         if(not event_permission_restricted_list):
    #             return True

    #         event_permission_restricted_list_user_check = event_permission_restricted_list.filter(user_id=user_id).exists()
    #         if(event_permission_restricted_list_user_check):
    #             return True
    return False

def module_permission_check(module_id, module_type, user_id, allowed_action_group_list, entity_id):
    '''
    General Function for checking module permissions
    '''
    is_permitted = False
    if(module_type=="event"):
        is_permitted = event_permission_check(module_id, user_id, allowed_action_group_list, entity_id)
    
    elif(module_type=="draft_event"):
        is_permitted = draft_event_permission_check(module_id, user_id, allowed_action_group_list, entity_id)
    
    # Same goes for other modules

    return is_permitted