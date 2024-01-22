# Generated by Django 4.1.7 on 2024-01-22 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('fauna', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('co2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankco2')),
                ('filtration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankfilter')),
                ('fish', models.ManyToManyField(blank=True, to='fauna.fish')),
                ('hardscape', models.ManyToManyField(to='catalog.tankhardscape')),
                ('invertebrates', models.ManyToManyField(blank=True, to='fauna.invertebrate')),
                ('lighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanklight')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scape.profile')),
                ('plants', models.ManyToManyField(blank=True, related_name='scape_plants', to='flora.plant')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanksize')),
                ('soil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanksoil')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankvolume')),
            ],
        ),
    ]
