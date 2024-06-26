# Generated by Django 3.1.7 on 2021-07-12 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
        ('quality_check', '0001_initial'),
        ('invoice', '0001_initial'),
        ('goods_receipt', '0001_initial'),
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('document_url', models.URLField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('payment_category', models.CharField(max_length=100)),
                ('base_payment_amount', models.DecimalField(decimal_places=10, max_digits=25, null=True)),
                ('payment_mode', models.CharField(max_length=100)),
                ('payment_reference', models.CharField(max_length=100)),
                ('applied_balance_amount', models.DecimalField(decimal_places=10, default=0, max_digits=25)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('comments', models.TextField(blank=True, max_length=500)),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id', to='enterprise.user')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
                ('from_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_entity_id', to='enterprise.entity')),
                ('to_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_entity_id', to='enterprise.entity')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBalance',
            fields=[
                ('balance_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('entry_type', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('used_amount', models.DecimalField(decimal_places=10, default=0, max_digits=25)),
                ('available_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('cashout_requested', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modefied_datetime', models.DateTimeField(auto_now=True)),
                ('deleted_datetime', models.DateTimeField(null=True)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.buyer')),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.currencycode')),
                ('prepayment_payment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment')),
                ('rejection_goods_receipt_entry_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods_receipt.goodsreceipt')),
                ('rejection_quality_check_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality_check.qualitycheck')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.seller')),
                ('source_purchase_order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase_order.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBalanceUsage',
            fields=[
                ('usage_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('usage_type', models.CharField(max_length=100)),
                ('used_amount', models.DecimalField(decimal_places=10, max_digits=25)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('adjusted_payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('balance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentbalance')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItemPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_applied', models.DecimalField(decimal_places=10, max_digits=25)),
                ('invoice_line_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoiceitem')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
        ),
    ]
