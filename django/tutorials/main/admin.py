from django.contrib import admin
from .models import Tutorial

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields=[
    #     "tutorial_title",
    #     "tutorial_published",
    #     "tutorial_content"
    # ]
    fieldsets=[
        ("Title",{"fields":["tutorial_title"]}),
        ("Date_Time",{"fields":["tutorial_published"]}),
        ("Content",{"fields":["tutorial_content"]})
    ]
admin.site.register(Tutorial,TutorialAdmin)
