# Generated by Django 3.1.7 on 2021-07-12 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_award_id', models.IntegerField(default=0)),
                ('draft_purchase_order_id', models.IntegerField(default=0)),
                ('purchase_order_id', models.IntegerField(default=0)),
                ('seller_bid_id', models.CharField(max_length=100)),
                ('award_creation_datetime', models.DateTimeField()),
                ('payment_terms_code', models.CharField(max_length=500)),
                ('subtotal', models.DecimalField(decimal_places=10, max_digits=25)),
                ('taxes', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_shipping_cost', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_other_charges', models.DecimalField(decimal_places=10, max_digits=25)),
                ('bulk_discount_percentage', models.DecimalField(decimal_places=10, max_digits=25)),
                ('bulk_discount_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total', models.DecimalField(decimal_places=10, max_digits=25)),
                ('deal_status', models.CharField(default='Deal Awarded', max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('deleted_datetime', models.DateTimeField(null=True)),
                ('approver_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award_approver', to='enterprise.user')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('creator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award_creator', to='enterprise.user')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('bid_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_bid_id', models.IntegerField(default=0)),
                ('bid_creator_entity_type', models.CharField(choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('seller_bid_id', models.CharField(max_length=100)),
                ('bid_creation_datetime', models.DateTimeField()),
                ('bid_valid_till_datetime', models.DateTimeField()),
                ('payment_terms_code', models.CharField(max_length=100)),
                ('seller_comments', models.TextField(blank=True, max_length=500)),
                ('rebid_request_comments', models.TextField(blank=True, max_length=500)),
                ('subtotal', models.DecimalField(decimal_places=10, max_digits=25)),
                ('taxes', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_shipping_cost', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_other_charges', models.DecimalField(decimal_places=10, max_digits=25)),
                ('bulk_discount_percentage', models.DecimalField(decimal_places=10, max_digits=25)),
                ('bulk_discount_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total', models.DecimalField(decimal_places=10, max_digits=25)),
                ('status', models.CharField(default='Response Submitted', max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('deleted_datetime', models.DateTimeField(null=True)),
                ('bid_creator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.user')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
            ],
        ),
        migrations.CreateModel(
            name='DraftAward',
            fields=[
                ('award_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_award_id', models.IntegerField(default=0)),
                ('draft_purchase_order_id', models.IntegerField(default=0)),
                ('purchase_order_id', models.IntegerField(default=0)),
                ('seller_bid_id', models.CharField(blank=True, max_length=100)),
                ('award_creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('payment_terms_code', models.CharField(blank=True, max_length=500)),
                ('subtotal', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('taxes', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_shipping_cost', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_other_charges', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('bulk_discount_percentage', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('bulk_discount_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('deal_status', models.CharField(default='Deal Awarded', max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('deleted_datetime', models.DateTimeField(null=True)),
                ('approver_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_award_approver', to='enterprise.user')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('creator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_award_creator', to='enterprise.user')),
                ('currency_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
            ],
        ),
        migrations.CreateModel(
            name='DraftBid',
            fields=[
                ('bid_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_bid_id', models.IntegerField(default=0)),
                ('bid_creator_entity_type', models.CharField(choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('seller_bid_id', models.CharField(blank=True, max_length=100)),
                ('bid_creation_datetime', models.DateTimeField(null=True)),
                ('bid_valid_till_datetime', models.DateTimeField(null=True)),
                ('payment_terms_code', models.CharField(max_length=100, null=True)),
                ('seller_comments', models.TextField(blank=True, max_length=500)),
                ('rebid_request_comments', models.TextField(blank=True, max_length=500)),
                ('subtotal', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('taxes', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_shipping_cost', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_other_charges', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('bulk_discount_percentage', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('bulk_discount_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('status', models.CharField(default='Response Due', max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('bid_creator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.user')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('currency_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.currencycode')),
            ],
        ),
        migrations.CreateModel(
            name='DraftEvent',
            fields=[
                ('event_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=500)),
                ('event_type', models.CharField(default='RFQ', max_length=500)),
                ('event_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('event_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('event_delivery_datetime', models.DateTimeField(blank=True, null=True)),
                ('payment_terms_code', models.CharField(blank=True, max_length=500, null=True)),
                ('created_by_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_billing_address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_draft', to='enterprise.address')),
                ('buyer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('buyer_shipping_address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_draft', to='enterprise.address')),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_draft', to='enterprise.user')),
                ('enterprise_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enterprise.enterprise')),
                ('last_modified_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_draft', to='enterprise.user')),
            ],
        ),
        migrations.CreateModel(
            name='DraftEventItem',
            fields=[
                ('event_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('buyer_item_id', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('meausrement_unit', models.CharField(blank=True, max_length=100)),
                ('desired_quantity', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('desired_price', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('opening_bid', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('allow_substitutes', models.BooleanField(default=False)),
                ('insurance_required', models.BooleanField(default=False)),
                ('post_to_global_market_place', models.BooleanField(default=False)),
                ('currency_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.currencycode')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftevent')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.item')),
                ('measurement_unit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.measurementunit')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_event_id', models.IntegerField(default=0)),
                ('event_name', models.CharField(max_length=500)),
                ('event_type', models.CharField(default='RFQ', max_length=500)),
                ('event_start_datetime', models.DateTimeField()),
                ('event_end_datetime', models.DateTimeField()),
                ('event_delivery_datetime', models.DateTimeField()),
                ('payment_terms_code', models.CharField(blank=True, max_length=500, null=True)),
                ('created_by_name', models.CharField(max_length=100)),
                ('created_by_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by_email', models.EmailField(max_length=100)),
                ('status', models.CharField(default='Ongoing', max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('deleted_datetime', models.DateTimeField(null=True)),
                ('buyer_billing_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_event', to='enterprise.address')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('buyer_shipping_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_event', to='enterprise.address')),
                ('created_by_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_event', to='enterprise.user')),
                ('enterprise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.enterprise')),
                ('last_modified_by_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_event', to='enterprise.user')),
            ],
        ),
        migrations.CreateModel(
            name='EventItem',
            fields=[
                ('event_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('buyer_item_id', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('meausrement_unit', models.CharField(blank=True, max_length=100)),
                ('desired_quantity', models.DecimalField(decimal_places=10, max_digits=25)),
                ('desired_price', models.DecimalField(decimal_places=10, max_digits=25)),
                ('opening_bid', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('allow_substitutes', models.BooleanField(default=False)),
                ('insurance_required', models.BooleanField(default=False)),
                ('post_to_global_market_place', models.BooleanField(default=False)),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.item')),
                ('measurement_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.measurementunit')),
            ],
        ),
        migrations.CreateModel(
            name='KeyMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft_event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.draftevent')),
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(default='', max_length=100)),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.attribute')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
            ],
        ),
        migrations.CreateModel(
            name='DraftEventItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=100)),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.attribute')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.drafteventitem')),
            ],
        ),
        migrations.CreateModel(
            name='DraftBidItem',
            fields=[
                ('bid_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity_offered', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('quantity_awarded', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('other_charges', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('shipping_managed_by', models.CharField(blank=True, choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('shipping_cost', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('seller_comments', models.TextField(blank=True, max_length=500)),
                ('bid_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftbid')),
                ('currency_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.currencycode')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
                ('measurement_unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.measurementunit')),
            ],
        ),
        migrations.AddField(
            model_name='draftbid',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='draftbid',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller'),
        ),
        migrations.CreateModel(
            name='DraftAwardItem',
            fields=[
                ('award_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity_offered', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('quantity_awarded', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('other_charges', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('shipping_managed_by', models.CharField(blank=True, choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('shipping_cost', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('award_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftaward')),
                ('currency_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.currencycode')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
                ('measurement_unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enterprise.measurementunit')),
            ],
        ),
        migrations.AddField(
            model_name='draftaward',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='draftaward',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller'),
        ),
        migrations.CreateModel(
            name='BidItem',
            fields=[
                ('bid_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity_offered', models.DecimalField(decimal_places=10, max_digits=25)),
                ('quantity_awarded', models.DecimalField(decimal_places=10, max_digits=25)),
                ('price', models.DecimalField(decimal_places=10, max_digits=25)),
                ('other_charges', models.DecimalField(decimal_places=10, max_digits=25)),
                ('shipping_managed_by', models.CharField(choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('shipping_cost', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('seller_comments', models.TextField(blank=True, max_length=500)),
                ('bid_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.bid')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
                ('measurement_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.measurementunit')),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='bid',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller'),
        ),
        migrations.CreateModel(
            name='AwardItem',
            fields=[
                ('award_line_item_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity_offered', models.DecimalField(decimal_places=10, max_digits=25)),
                ('quantity_awarded', models.DecimalField(decimal_places=10, max_digits=25)),
                ('price', models.DecimalField(decimal_places=10, max_digits=25)),
                ('other_charges', models.DecimalField(decimal_places=10, max_digits=25)),
                ('shipping_managed_by', models.CharField(choices=[('B', 'Buyer'), ('S', 'Seller')], max_length=100)),
                ('shipping_cost', models.DecimalField(decimal_places=10, max_digits=25)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('award_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.award')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
                ('measurement_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.measurementunit')),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='award',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller'),
        ),
        migrations.CreateModel(
            name='EventItemSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_approval_required', models.BooleanField(default=False)),
                ('approved_by_buyer', models.BooleanField(null=True)),
                ('invitation_status', models.CharField(blank=True, max_length=100, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventitem')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller')),
            ],
            options={
                'unique_together': {('event_line_item_id', 'seller_id')},
            },
        ),
        migrations.CreateModel(
            name='DraftEventItemSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_approval_required', models.BooleanField(default=False)),
                ('approved_by_buyer', models.BooleanField(null=True)),
                ('invitation_status', models.CharField(blank=True, max_length=100, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftevent')),
                ('event_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.drafteventitem')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller')),
            ],
            options={
                'unique_together': {('event_line_item_id', 'seller_id')},
            },
        ),
        migrations.CreateModel(
            name='DraftBidItemTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('bid_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftbiditem')),
            ],
            options={
                'unique_together': {('bid_line_item_id', 'tax_name')},
            },
        ),
        migrations.CreateModel(
            name='DraftAwardItemTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('award_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.draftawarditem')),
            ],
            options={
                'unique_together': {('award_line_item_id', 'tax_name')},
            },
        ),
        migrations.CreateModel(
            name='BidItemTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=10, max_digits=25)),
                ('bid_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.biditem')),
            ],
            options={
                'unique_together': {('bid_line_item_id', 'tax_name')},
            },
        ),
        migrations.CreateModel(
            name='AwardItemTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=10, max_digits=25)),
                ('award_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.awarditem')),
            ],
            options={
                'unique_together': {('award_line_item_id', 'tax_name')},
            },
        ),
    ]
