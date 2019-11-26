from djongo import models
from django import forms


# python manage.py makemigrations vis_app
# python manage.py migrate vis_app
# python manage.py migrate

class PlotObject(models.Model):
    formula = models.CharField(max_length=100)
    start = models.FloatField()
    end = models.FloatField()
    step = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def share_url(self):
        return f'http://127.0.0.1:8000/vis-shared/{self.id}'


class GraphConnection(models.Model):
    connection_from = models.IntegerField()
    connection_to = models.IntegerField()


class GraphConnectionFrom(forms.ModelForm):
    class Meta:
        model = GraphConnection
        fields = ('connection_from', 'connection_to')


class GraphObject(models.Model):
    connections = models.ArrayModelField(model_container=GraphConnection, model_form_class=GraphConnectionFrom)

# Create your models here.
