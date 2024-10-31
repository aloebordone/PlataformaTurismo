from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(
        upload_to="../gps_simulation/media/city_images", null=True, blank=True
    )

    def __str__(self):
        return self.name

    
    def __str__(self):
        return self.name


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
