# Generated by Django 5.2.3 on 2025-06-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPushSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.URLField()),
                ('auth', models.CharField(max_length=255)),
                ('p256dh', models.CharField(max_length=255)),
            ],
        ),
    ]
