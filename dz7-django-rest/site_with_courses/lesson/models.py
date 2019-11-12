from django.db import models


# Create your models here.
class Lesson(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=900)
    lesson_date = models.DateField(blank=True)

    def __str__(self):
        return "Урок:{}".format(self.name)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
