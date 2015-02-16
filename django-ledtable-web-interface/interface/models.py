from django.db import models

class Animation(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Option(models.Model):
    INTEGER = 'INT'
    COLOR = 'COLOR'
    COLOR_LIST = 'COLORS'
    OPTION_TYPES = (
        (INTEGER, 'Integer'),
        (COLOR, 'Color'),
        (COLOR_LIST, 'ColorList')
    )  
    animation = models.ForeignKey(Animation)
    name = models.CharField(max_length=100)
    option_type = models.CharField(max_length=6, choices=OPTION_TYPES)
    def __str__(self):              # __unicode__ on Python 2
        return self.name + ' ' +self.option_type

