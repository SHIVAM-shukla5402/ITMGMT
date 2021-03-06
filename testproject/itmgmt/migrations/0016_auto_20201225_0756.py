# Generated by Django 3.1.4 on 2020-12-25 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itmgmt', '0015_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount_apply_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('timestamp_lastupdated', models.DateTimeField(auto_now=True)),
                ('docstatus', models.BooleanField(default=True)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Discount_value_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('timestamp_lastupdated', models.DateTimeField(auto_now=True)),
                ('docstatus', models.BooleanField(default=True)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='item_discount',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item_discount',
            name='qty',
        ),
        migrations.AddField(
            model_name='item_discount',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmgmt.company'),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='costcenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmgmt.costcenter'),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='discount_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='is_purchase',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='is_salable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='max_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='max_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='min_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='min_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='valid_discount_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='valid_end_discount_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmgmt.warehouse'),
        ),
        migrations.AlterField(
            model_name='item_discount',
            name='entry_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item_discount',
            name='discount_value_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmgmt.discount_value_type'),
        ),
        migrations.AlterField(
            model_name='item_discount',
            name='discount_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmgmt.discount_apply_on'),
        ),
    ]
