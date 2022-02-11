from django.db import models


# Create your models here.
class Technology(models.Model):
    description = models.CharField(max_length=20)
    percentage = models.IntegerField()
    logo = models.FilePathField()

    def __str__(self):
        return self.description


class Experience(models.Model):
    job = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    init_date = models.DateField()
    finish_date = models.DateField(null=True)

    def __str__(self):
        return "{} at {}".f(self.job, self.company)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    image = models.FilePathField(null=True)

    def __str__(self):
        return self.title
