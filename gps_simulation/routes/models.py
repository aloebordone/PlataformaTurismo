#importación de librerias( importa el módulo models de Django,post_save señal, receiver se ejecutarán en respuesta a un signal, UniqueConstraint para definir restricciones de unicidad )
from django.db import models 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import UniqueConstraint


class City(models.Model): #crea modelo City en la base de datos
    name = models.CharField(max_length=100, unique=True, blank = False) #define como será el campo nombre: cantidad de palabras, no puede repetirse la ciudad y no puede estar en blacno su nombre
    description = models.TextField(null=True) #define el formato del campo descripcion
    population = models.IntegerField(null=True, unique=False) #define formato de campo population

    
    def __str__(self): #crea metodo str para mostrar de manera legible al usuario nombre, descripcion y habitantes
        return  f"{self.name} - ({self.description}) - ({self.population} habitantes)"


class Route(models.Model): #crea modelo Route en la bse de datos
    #define una relacion entre clase ruta y clase city que recibe el nombre de star_city y le define un comportamento en cascada para eliminacion
    start_city = models.ForeignKey(
        City, related_name="route_start", on_delete=models.CASCADE
    )
    end_city = models.ForeignKey(
        City, related_name="route_end", on_delete=models.CASCADE
    )
    #asigna a distancia un float de la bse de datos
    distance = models.FloatField()

    #crea metodo str para mostrar de manera legible al usuario
    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"
    
    #define una restricción de unicidad para la clase 
    class Meta:
        constraints = [
            UniqueConstraint(fields=['start_city', 'end_city'], name='unique_route')
        ]

@receiver(post_save, sender=Route) #indica que la función create_inverse_route escucha un evento post_save del modelo ruta
def create_inverse_route(sender, instance, created, **kwargs): #esta funcion dispara el post_save
    if created: #si se acaba de crear la instancia
        Route.objects.get_or_create(# Intentar obtener la ruta inversa. si no la obtiene la crea
            start_city=instance.end_city,
            end_city=instance.start_city,
            defaults={'distance': instance.distance}
        )