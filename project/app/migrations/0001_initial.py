# Generated by Django 5.0.6 on 2024-06-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Product_descip', models.CharField(max_length=200)),
                ('Product_price', models.IntegerField()),
                ('Product_image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'AddProduct',
            },
        ),
    ]
