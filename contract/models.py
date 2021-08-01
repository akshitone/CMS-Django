from django.db import models

# Type of service contract
TYPE_OF_SERVICE = [(1, 'Platinum'), (2, 'Gold'), (3, 'Silver'), (4, 'Bronze')]


# Contract model
class Constract(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField()
    contact = models.IntegerField()
    type = models.IntegerField(choices=TYPE_OF_SERVICE, default=4)
