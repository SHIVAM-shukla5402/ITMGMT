# Generated by Django 3.1.4 on 2020-12-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itmgmt', '0008_auto_20201223_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_nature',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account_nature',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='asset',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='asset',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='balance_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='balance_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='department',
            name='disable',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='docstatus',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='discount_on',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discount_on',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discount_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discount_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equity',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equity',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frozen',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frozen',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gst_category',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gst_category',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='income',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='income',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='is_group',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='is_group',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_rate_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_rate_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='liability',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='liability',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parent_account',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parent_account',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relationship',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relationship',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='root_account_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='root_account_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='root_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='root_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tax',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tax',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tax_type',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tax_type',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer_supplier',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer_supplier',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_fixed_asset',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_purchase',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_salable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item_discount',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item_discount',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item_valuation_rate',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item_valuation_rate',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='docstatus',
            field=models.BooleanField(default=False),
        ),
    ]
