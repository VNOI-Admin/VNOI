from django.contrib import admin
from .models import Problem, ProblemType

admin.site.register(ProblemType)
admin.site.register(Problem)
