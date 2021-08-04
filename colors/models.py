from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Range(models.Model):
    name = models.CharField(max_length=20)
    range_start = models.IntegerField()
    range_stop = models.IntegerField()
    suffix = models.CharField(max_length=10, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='ranges')
