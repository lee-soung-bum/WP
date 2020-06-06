from django.contrib import admin
from community.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','userid','password')

class Choice2002Inline(admin.TabularInline):
    model = Choice2002
    extra = 2

class Question2002Admin(admin.ModelAdmin):
    inlines = [Choice2002Inline]

class Choice2010Inline(admin.TabularInline):
    model = Choice2010
    extra = 2

class Question2010Admin(admin.ModelAdmin):
    inlines = [Choice2010Inline]

class ChoiceNowInline(admin.TabularInline):
    model = ChoiceNow
    extra = 2

class QuestionNowAdmin(admin.ModelAdmin):
    inlines = [ChoiceNowInline]

class ChoiceBestInline(admin.TabularInline):
    model = ChoiceBest
    extra = 2

class QuestionBestAdmin(admin.ModelAdmin):
    inlines = [ChoiceBestInline]

admin.site.register(User, UserAdmin)
admin.site.register(Question2002, Question2002Admin)
admin.site.register(Choice2002)
admin.site.register(Question2010, Question2010Admin)
admin.site.register(Choice2010)
admin.site.register(QuestionNow, QuestionNowAdmin)
admin.site.register(ChoiceNow)
admin.site.register(QuestionBest, QuestionBestAdmin)
admin.site.register(ChoiceBest)
