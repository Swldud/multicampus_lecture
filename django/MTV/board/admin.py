from django.contrib import admin
from.models import Notice


# Register your models here.

# 앱에 들어있는 model을 등록해주어야 한다.
admin.site.register(Notice)