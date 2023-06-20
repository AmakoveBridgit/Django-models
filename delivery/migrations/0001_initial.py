# Generated by Django 2.2.12 on 2023-06-20 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('deliverytime', models.DateTimeField(auto_now=True)),
                ('isdelivered', models.BooleanField(default=False)),
            ],
        ),
    ]
