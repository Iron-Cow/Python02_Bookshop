from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=1024, null=True, blank=True)
    price = models.PositiveIntegerField()
    sale = models.BooleanField(default=False)

    @property
    def owner_card(self):
        return self.owner.customer_card
