# Generated by Django 5.0.6 on 2024-06-09 14:49

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Duct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Manhole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('description', models.TextField(blank=True, null=True)),
                ('cable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segments', to='network.cable')),
                ('end_manhole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_segments', to='network.manhole')),
                ('start_manhole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_segments', to='network.manhole')),
            ],
        ),
        migrations.CreateModel(
            name='SubDuct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('duct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subducts', to='network.duct')),
            ],
        ),
        migrations.AddField(
            model_name='manhole',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manholes', to='network.track'),
        ),
        migrations.AddField(
            model_name='duct',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ducts', to='network.track'),
        ),
    ]
