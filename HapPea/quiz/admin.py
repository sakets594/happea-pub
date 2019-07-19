from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Plot)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserResponse)
admin.site.register(UserQuestionnaire)
admin.site.register(ResponseOption)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(QuizImage)