# Generated by Django 5.0.6 on 2024-06-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('order_id', models.CharField(max_length=1000)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=1000)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]