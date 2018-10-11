# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User
from .models import Answer
from .models import Tag
from .models import Question

admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Question)

