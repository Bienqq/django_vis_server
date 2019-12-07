# Generated by Django 2.2.6 on 2019-12-07 18:49

from django.db import migrations, models
import djongo.models.fields
import vis_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connections', djongo.models.fields.ArrayModelField(model_container=vis_app.models.GraphConnection)),
                ('nodes', djongo.models.fields.ArrayModelField(model_container=vis_app.models.GraphNode)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlotObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=100)),
                ('start', models.FloatField()),
                ('end', models.FloatField()),
                ('step', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
