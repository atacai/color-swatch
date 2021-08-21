from django.db import models


class ColorSpace(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Attribute(models.Model):
    name = models.CharField(max_length=20)
    range_start = models.IntegerField()
    range_stop = models.IntegerField()
    suffix = models.CharField(max_length=10, blank=True)
    color_space = models.ForeignKey(ColorSpace, on_delete=models.CASCADE, related_name='attributes')
