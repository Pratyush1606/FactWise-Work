from django.urls import reverse
import json
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from enterprise.models import *
from enterprise.serializers import *
from event.models import *
from event.serializers import *

class PostEventDraftEventViewTest(APITestCase):
    def setUp(self):
        '''
        Populating test db 
        Entering a event with event_id 1
        '''
        Enterprise.objects.create(enterprise_name="ENT 1")
        self.enterprise = Enterprise.objects.get(enterprise_id=1)
        entity_data1 = {
            "enterprise_id": self.enterprise,
            "entity_type": "IT",
            "entity_name": "Apple",
            "entity_primary_address": "xyz",
            "entity_primary_email": "apple@gmail.com"
        }
        Entity.objects.create(**entity_data1)
        self.entity1 = Entity.objects.get(entity_id=1)
        buyer_data = {
            "buyer_id" : self.entity1
        }
        Buyer.objects.create(**buyer_data)
        self.buyer = Buyer.objects.get(buyer_id=1)
        user_data = {
            "enterprise_id": self.enterprise,
            "user_email": "apple1@gmail.com",
            "user_firstname": "Pratyush",
            "user_lastname": "Jaiswal",
            "user_phonenumber": "xxxxxx91"
        }
        User.objects.create(**user_data)
        self.user = User.objects.get(user_id=1)
        address_data1 = {
            "address_nickname": "Berkeley Office",
            "country": "USA",
            "address1": "215 Dwight Way, Berkeley, CA 97074",
            "city" : "berkeley",
            "postal_code" : 97074
        }
        Address.objects.create(**address_data1)
        self.address1 = Address.objects.get(address_id=1)
        address_data2 = {
            "address_nickname": "New York Headquarters",
            "country": "USA",
            "address1": "156 Street Way, New York, NY 67809",
            "city" : "New York",
            "postal_code" : 67809
        }
        Address.objects.create(**address_data2)
        self.address2 = Address.objects.get(address_id=2)
        event_data = {
           "enterprise_id": self.enterprise, 
           "buyer_id" : self.buyer,
           "event_name": "Buy", 
           "event_type": "RFQ", 
           "event_start_datetime": "2021-05-17T09:49:43.583737Z", 
           "event_end_datetime": "2021-05-17T09:49:43.583737Z", 
           "buyer_billing_address_id": self.address1, 
           "buyer_shipping_address_id": self.address2, 
           "event_delivery_datetime": "2021-05-17T09:49:43.583737Z", 
           "payment_terms_code": "USD", 
           "created_by_user_id": self.user, 
           "created_by_name": "Pratyush", 
           "created_by_phone": "xxxxxx991", 
           "created_by_email": "jaiswalprat@gmail.com", 
           "status": "Ongoing", 
           "last_modified_by_user_id": self.user
        }
        Event.objects.create(**event_data)
        self.event = Event.objects.get(event_id=1)
        Enterprise.objects.create(enterprise_name="ENT 2")
        self.enterprise2 = Enterprise.objects.get(enterprise_id=2)
        entity_data2 = {
            "enterprise_id": self.enterprise2,
            "entity_type": "IT1",
            "entity_name": "Apple1",
            "entity_primary_address": "xyz1",
            "entity_primary_email": "apple1@gmail.com"
        }
        Entity.objects.create(**entity_data2)
        self.entity2 = Entity.objects.get(entity_id=2)
        seller_data1 = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data1)
        self.seller1 = Seller.objects.get(seller_id=2)
        Enterprise.objects.create(enterprise_name="ENT 3")
        self.enterprise3 = Enterprise.objects.get(enterprise_id=3)
        entity_data3 = {
            "enterprise_id": self.enterprise3,
            "entity_type": "IT2",
            "entity_name": "Apple2",
            "entity_primary_address": "xyz2",
            "entity_primary_email": "apple2@gmail.com"
        }
        Entity.objects.create(**entity_data3)
        self.entity2 = Entity.objects.get(entity_id=3)
        seller_data2 = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data2)
        self.seller2 = Seller.objects.get(seller_id=3)
        measurement_unit_data = {
            "measurement_unit_primary_name" : "meter",
            "measurement_unit_category" : "length",
            "measurement_unit_value_type" : "Dec"
        }
        MeasurementUnit.objects.create(**measurement_unit_data)
        self.measurement_unit_id = MeasurementUnit.objects.get(measurement_unit_id=1)
        CurrencyCode.objects.create(currency_code="USD")
        self.currency_code = CurrencyCode.objects.get(currency_code="USD")
        item_data = {
            "item_name": "IPhone",
            "item_description": "An Apple Product"
        }
        Item.objects.create(**item_data)
        self.item = Item.objects.get(item_id=1)
        event_item_data = {
            "currency_code": self.currency_code,
            "item_id": self.item, 
            "event_id" : self.event,
            "buyer_item_id": "200012 Iphone - Black", 
            "description": "Just an exp", 
            "measurement_unit_id": self.measurement_unit_id, 
            "meausrement_unit": "meters", 
            "desired_quantity": 100, 
            "desired_price": 950, 
            "opening_bid": 950, 
            "total_amount": 100000
        }
        EventItem.objects.create(**event_item_data)
        self.event_item = EventItem.objects.get(event_line_item_id=1)
        attribute_data = {
            "attribute_name": "Density",
            "attribute_value_type": "enum"
        }
        Attribute.objects.create(**attribute_data)
        self.attribute = Attribute.objects.get(attribute_id=1)
        event_item_attribute_data = {
            "event_line_item_id" : self.event_item,
            "attribute_id" : self.attribute,
            "attribute_value" : "16"
        }
        EventItemAttribute.objects.create(**event_item_attribute_data)
        data = [
            {
                "event_line_item_id" : self.event_item,
                "event_id" : self.event,
                "seller_id" : self.seller1,
                "buyer_approval_required" : True,
                "approved_by_buyer" : True
            },
            {
                "event_line_item_id" : self.event_item,
                "event_id" : self.event,
                "seller_id" : self.seller2,
                "buyer_approval_required" : True,
                "approved_by_buyer" : True
            }
        ]
        EventItemSeller.objects.bulk_create(EventItemSeller(**x) for x in data)
        # Posting user entity
        self.user_entity_1 = UserEntity.objects.create(user_id=self.user, entity_id=self.entity1)

        # Posting username and password
        user_auth_data = {
            "username": "Matt",
            "password": make_password("123456"),
            "user_id": self.user
        }
        self.user_auth_1 = UserAuth.objects.create(**user_auth_data)
        # Posting user permissions
        user_permissions_1 = [
            {
                "user_entity_relationship_id": self.user_entity_1,
                "action_api_group": "buyer_event",
            },
            {   
                "user_entity_relationship_id": self.user_entity_1,
                "action_api_group" : "buyer_event_creation" 
            },
            {  
                "user_entity_relationship_id": self.user_entity_1, 
                "action_api_group" : "buyer_event_management" 
            },
            {  
                "user_entity_relationship_id": self.user_entity_1, 
                "action_api_group" : "buyer_event_admin" 
            }
        ]
        UserPermission.objects.bulk_create(UserPermission(**permission) for permission in user_permissions_1)
        
        # Logging in the user 1
        self.client.force_authenticate(user=self.user_auth_1)

    def test_post_valid_shift_event_to_draft_event(self):
        '''
        Getting event with ID 1
        '''
        response = self.client.post(reverse("event:shift_event_to_draft_event" , args=[1]))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["draft_event_info"]["event_id"], 1)
        self.assertEqual(response.data["event_item_list"][0]["draft_item_info"]["event_line_item_id"], 1)
        self.assertEqual(response.data["event_item_list"][0]["item_attribute"][0]["attribute_id"], 1)
        self.assertEqual(response.data["event_item_list"][0]["item_seller"][1]["seller_id"], 3)
        response = self.client.get(reverse("event:key_mappings"))
        self.assertEqual(response.data[0]["event_id"], 1)
        self.assertEqual(response.data[0]["draft_event_id"], 1)
        response = self.client.post(reverse("event:shift_event_to_draft_event" , args=[1]))
        self.assertEqual(response.data, "draft event already exists")


    def test_post_invalid_shift_event_to_draft_event(self):
        '''
        Getting event with ID 2, which does not exist
        '''
        response = self.client.post(reverse("event:shift_event_to_draft_event" , args=[2]))
        self.assertEqual(response.status_code, 404)
    
    