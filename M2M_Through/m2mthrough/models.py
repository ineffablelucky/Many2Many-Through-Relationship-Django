from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Standard(models.Model):
    class_number = models.PositiveSmallIntegerField(unique=True, validators=[MinValueValidator(1),
                                                                              MaxValueValidator(12)])
    total_students = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}'.format(self.class_number)

class Teacher(models.Model):
    name = models.CharField(max_length=20, unique=True)
    table = models.ManyToManyField(Standard, through='Timetable', through_fields=('teacher','standard'),)

    def __str__(self):
        return '{}'.format(self.name)

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ManyToManyField.through
class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return '{} in standard {}'.format(self.teacher,self.standard)