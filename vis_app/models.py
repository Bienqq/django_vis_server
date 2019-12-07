from djongo import models


# python manage.py migrate
# python manage.py makemigrations vis_app
# python manage.py migrate vis_app


class PlotObject(models.Model):
    formula = models.CharField(max_length=100)
    start = models.FloatField()
    end = models.FloatField()
    step = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def share_url(self):
        return f'http://127.0.0.1:8000/vis-shared-plot/{self.id}'


class GraphConnection(models.Model):
    connection_from = models.CharField(max_length=100)
    connection_to = models.CharField(max_length=100)

    def __repr__(self):
        return f'{{connection_from:{self.connection_from}, connection_to:{self.connection_to}}}'

    class Meta:
        abstract = True


class GraphNode(models.Model):
    node = models.CharField(max_length=100)

    def __repr__(self):
        return f'"{self.node}"'

    class Meta:
        abstract = True


class GraphObject(models.Model):
    connections = models.ArrayModelField(model_container=GraphConnection)
    nodes = models.ArrayModelField(model_container=GraphNode)
    date_created = models.DateTimeField(auto_now_add=True)

    def share_url(self):
        return f'http://127.0.0.1:8000/vis-shared-graph/{self.id}'

# Create your models here.
