# Generated by Django 5.0.4 on 2024-04-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efit', '0003_alter_membership_email_alter_membership_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
