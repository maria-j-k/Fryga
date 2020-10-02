from django.db import models
from django.utils import timezone

# Create your models here.


class Bank(models.Model):
    VERY_BAD = -2
    BAD = -1
    NEUTRAL = 0
    GOOD = 1
    VERY_GOOD = 2
    RATING_CHOICES = [
        (VERY_BAD, 'bardzo źle'),
        (BAD, 'kiepsko'),
        (NEUTRAL, 'średnio'),
        (GOOD, 'dobrze'),
        (VERY_GOOD, 'bardzo dobrze'), ]
    added = models.DateTimeField(auto_now_add=True)
    day = models.DateField('data ćwiczenia')
    duration = models.PositiveIntegerField('czas trwania / liczba powtórzeń')
    place = models.CharField('miejsce', max_length=32)
    place_description = models.CharField(
        'opis miejsca', max_length=128, blank=True)
    description = models.TextField('opis ćwiczenia')
    photo = models.ImageField('zdjęcie', blank=True)
    film = models.URLField('nagranie', blank=True)
    rating = models.SmallIntegerField(
        'ocenia zachowania psa',
        choices=RATING_CHOICES,
        default=NEUTRAL)

    class Meta:
        ordering = ['-day']

    def __str__(self):
        return f'Ćwiczenie z {self.day}, miejsce: {self.place}'
