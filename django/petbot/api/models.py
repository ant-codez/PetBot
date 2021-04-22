from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"
    username = models.CharField(max_length=20)
    eggs = models.IntegerField(default = 0)
    discord_id = models.BigIntegerField(default = 0)
    coins = models.IntegerField(default = 0)

class Pet(models.Model):
    class Meta:
        db_table = "pet"
    pet_name = models.TextField()
    species = models.TextField()
    discord_id = models.BigIntegerField()
    color = models.TextField()
    closeness = models.IntegerField()
    size = models.TextField()
    ability_type = models.TextField()
    rarity = models.TextField()
    owner = models.TextField()
    stats = ArrayField(models.IntegerField())