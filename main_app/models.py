from django.db import models

# Create your models here.

RATINGS = (
    ('1', 'One Star'),
    ('2', 'Two Stars'),
    ('3', 'Three Stars'),
    ('4', 'Four Stars'),
    ('5', 'Five Stars')
    )

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    time = models.IntegerField('Hours Played')

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.CharField(max_length=50)
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)