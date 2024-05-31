# Generated by Django 5.0.4 on 2024-04-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('membership_type', models.CharField(choices=[('Basic', 'Basic'), ('Ultimate', 'Ultimate'), ('Premium', 'Premium')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
