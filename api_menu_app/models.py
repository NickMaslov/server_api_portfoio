from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(
        #  claudinary has up to 1024 characters
        max_length=255,
        default="https://media.timeout.com/images/105802468/750/562/image.jpg",
    )
    number_of_tables = models.IntegerField(default=1)
    font = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}/{}".format(self.owner.username, self.name)
