from django.urls import reverse
import json
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.utils import timezone

from enterprise.models import *
from enterprise.serializers import *
from event.models import *
from event.serializers import *

class DraftEventItemSellerModelViewTest(APITestCase):
    def setUp(self):
        '''
        Populating test db 
        Entering a draft_event_item_seller with event_line_item_id 1
        '''
        Enterprise.objects.create(enterprise_name="ENT 1")
        self.enterprise = Enterprise.objects.get(enterprise_id=1)
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
        draft_event_data = {
           "enterprise_id": self.enterprise, 
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
           "status": "Draft", 
           "last_modified_by_user_id": self.user
        }
        DraftEvent.objects.create(**draft_event_data)
        self.draft_event = DraftEvent.objects.get(event_id=1)
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
        self.entity2 = Entity.objects.get(entity_id=1)
        seller_data = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data)
        self.seller = Seller.objects.get(seller_id=1)
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
        draft_event_item_data = {
            "currency_code": self.currency_code,
            "item_id": self.item, 
            "event_id" : self.draft_event,
            "buyer_item_id": "200012 Iphone - Black", 
            "description": "Just an exp", 
            "measurement_unit_id": self.measurement_unit_id, 
            "meausrement_unit": "meters", 
            "desired_quantity": 100, 
            "desired_price": 950, 
            "opening_bid": 950, 
            "total_amount": 100000
        }
        DraftEventItem.objects.create(**draft_event_item_data)
        self.draft_event_item = DraftEventItem.objects.get(event_line_item_id=1)
        data = {
            "event_line_item_id" : self.draft_event_item,
            "event_id" : self.draft_event,
            "seller_id" : self.seller
        }
        DraftEventItemSeller.objects.create(**data)

    def test_get_valid_draft_event_item_seller(self):
        '''
        Getting draft_event_item_seller with ID 1
        '''
        response = self.client.get(reverse("event:draft_event_item_seller" , args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["event_id"], 1)
        self.assertEqual(response.data[0]["seller_id"], 1)

    def test_get_invalid_draft_event_item_seller(self):
        '''
        Getting draft_event_item_seller with ID 2, which does not exist
        '''
        response = self.client.get(reverse("event:draft_event_item_seller" , args=[2]))
        self.assertEqual(response.status_code, 404)
    
    def test_post_valid_draft_event_item_seller(self):
        '''
        Posting a new draft_event_item_seller
        '''
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
        self.entity2 = Entity.objects.get(entity_id=2)
        seller_data = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data)
        self.seller = Seller.objects.get(seller_id=2)
        data = {
            "seller_id" : 2
        }
        response = self.client.post(reverse("event:draft_event_item_seller" , args=[1]), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[0]["event_id"], 1)
        self.assertEqual(response.data[0]["seller_id"], 2)
    
    def test_post_invalid_draft_event_item_seller(self):
        '''
        Posting a new draft_event_item_seller with invalid info
        '''
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
        self.entity2 = Entity.objects.get(entity_id=2)
        seller_data = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data)
        self.seller = Seller.objects.get(seller_id=2)
        data = {
            "seller_id" : 3
        }
        response = self.client.post(reverse("event:draft_event_item_seller" , args=[1]), data)
        self.assertEqual(response.status_code, 400)

    def test_patch_valid_item_seller(self):
        '''
        Patching item_seller with ID 1 with name
        '''
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
        self.entity2 = Entity.objects.get(entity_id=2)
        seller_data = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data)
        self.seller = Seller.objects.get(seller_id=2)
        data = [
            {
                "seller_id" : 1
            },
            {
                "seller_id" : 2
            }
        ]
        response = self.client.patch(reverse("event:draft_event_item_seller" , args=[1]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[0]["event_id"], 1)
        self.assertEqual(response.data[0]["seller_id"], 1)
        self.assertEqual(response.data[1]["seller_id"], 2)
    
    def test_patch_invalid_item_seller(self):
        '''
        Patching invalid info
        '''
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
        self.entity2 = Entity.objects.get(entity_id=2)
        seller_data = {
            "seller_id" : self.entity2
        }
        Seller.objects.create(**seller_data)
        self.seller = Seller.objects.get(seller_id=2)
        data = [
            {
                "seller_id" : 3
            },
            {
                "seller_id" : 2
            }
        ]
        response = self.client.patch(reverse("event:draft_event_item_seller" , args=[1]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.patch(reverse("event:draft_event_item_seller" , args=[3]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)