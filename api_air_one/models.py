from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="City")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["name"]


class Plane(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Plane number")
    travel_time = models.PositiveSmallIntegerField(verbose_name="Travel time, minutes")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="from_city_set",
        verbose_name="departures from",
    )
    to_city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="to_city_set",
        verbose_name="arrives in",
    )

    def __str__(self):
        return f"Plane № {self.name}  {self.from_city} to {self.to_city}"

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Departing and arrival cities are the same")
        # checking that we don't have exactly same plane record(which is optional)
        qs = Plane.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Change travel time")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Plane"
        verbose_name_plural = "Planes"
        ordering = ["travel_time"]


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Route name")
    travel_times = models.PositiveSmallIntegerField(verbose_name="Total Travel Time")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_from_city_set",
        verbose_name="Departing from a city",
    )
    to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_to_city_set",
        verbose_name="Arriving in a city",
    )
    planes = models.ManyToManyField(Plane, verbose_name="List of Planes")

    def __str__(self):
        return f"Route number {self.name} from {self.from_city} to {self.to_city}"

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        ordering = ["travel_times"]
