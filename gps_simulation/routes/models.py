from django.db import models
from django.db.models.signals import post_save
from .models import Route

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, blank = False)
    description = models.TextField(null=True)
    population = models.IntegerField(null=True, unique=False)

    
    def __str__(self):
        return  f"{self.name} - ({self.description}) - ({self.population} habitantes)"


class Route(models.Model):
    start_city = models.ForeignKey(
        City, related_name="route_start", on_delete=models.CASCADE
    )
    end_city = models.ForeignKey(
        City, related_name="route_end", on_delete=models.CASCADE
    )
    distance = models.FloatField()

    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"

    def create_inverse_route(sender, instance, created, **kwargs):
        if created:
            inverse_route = Route.objects.create(
            start_city=instance.end_city,
            end_city=instance.start_city,
            distance=instance.distance,
        )
    post_save.connect(create_inverse_route, sender=Route)