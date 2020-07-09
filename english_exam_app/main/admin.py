from django.contrib import admin

from .models import Diary, TextBook, Question, Answer


admin.site.register(Diary)
admin.site.register(TextBook)
admin.site.register(Question)
admin.site.register(Answer)
