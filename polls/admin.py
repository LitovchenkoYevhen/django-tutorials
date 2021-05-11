from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',) # добавляем в админку в список вопросов столбец с датой
    list_display_links= ('question_text', 'pub_date',) # делаем строки ссылками
    search_fields = ('question_text', 'pub_date',)



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(QuestionAdmin)