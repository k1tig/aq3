# Generated by Django 5.0.1 on 2024-01-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0001_initial'),
        ('scape', '0002_alter_profile_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scape',
            name='plants',
            field=models.ManyToManyField(blank=True, related_name='plants', to='flora.plant'),
        ),
    ]