from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=400)
    date_start_course = models.DateField(blank=True)
    date_end_course = models.DateField(blank=True)
    teacher = models.ManyToManyField('teacher.Teacher')
    price = models.FloatField(blank=True)
    studients = models.ManyToManyField('profile_user.Profile',  blank=True, related_name='courses')

    def __str__(self):
        return "Курс {} стартует {}.".format(self.name, self.date_start_course)

    def planned_duration(self):
        return self.date_end_course - self.date_start_course

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
