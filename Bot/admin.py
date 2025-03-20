from django.contrib import admin
from .models import FAQ, UnansweredQuestion

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
    search_fields = ("question",)

@admin.register(UnansweredQuestion)
class UnansweredQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "timestamp")
    search_fields = ("question",)
