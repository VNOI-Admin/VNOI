from django.db import models


class ProblemType(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    type = models.ForeignKey(ProblemType, null=False, blank=False)

    def __str__(self):
        return self.code + '(' + self.name + ')'

