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


class Category(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}/{}".format(self.place, self.name)


class MenuItem(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="menu_items"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "{}/{}".format(self.category, self.name)


class Order(models.Model):
    PROCESSING_STATUS = "processing"
    COMPLETED_STATUS = "completed"
    STATUSES = (
        (PROCESSING_STATUS, "Processing"),
        (COMPLETED_STATUS, "Completed"),
    )

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    table = models.CharField(max_length=2)
    detail = models.TextField()
    payment_intent = models.CharField(max_length=255)
    amount = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=STATUSES, default=PROCESSING_STATUS
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}/{}/${}".format(self.place, self.table, self.amount)
