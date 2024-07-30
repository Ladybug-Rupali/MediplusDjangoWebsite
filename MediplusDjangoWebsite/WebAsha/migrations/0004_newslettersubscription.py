# Generated by Django 5.0.3 on 2024-07-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAsha', '0003_booking_time_alter_booking_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]