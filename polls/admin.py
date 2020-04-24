from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# TEK TEK EKLEMEN LAZIM.
# admin.site.register(Question)
# admin.site.register(Choice)

# heading title name
admin.site.site_header = "Anketör Admin Paneli"
admin.site.site_title = "Anketör Admin"
admin.site.index_title = "Anket Uygulamasına Hoş Geldiniz !"


# Eger cevapları da asagida gostermek istiyorsan
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'],
                                       'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
