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
    description = models.TextField(null=True)
    init_date = models.DateField()
    finish_date = models.DateField(null=True)

    def get_title(self):
        return "{} at {}".format(self.job, self.company)

    def get_period(self):
        return "{} - {}".format(self.init_date.strftime("%b %Y"), self.finish_date.strftime("%b %Y") if self.finish_date else 'Current')


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(null=True)
    image = models.FilePathField(null=True)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title
