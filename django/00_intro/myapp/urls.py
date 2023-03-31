
from django.urls import path

from . import views

urlpatterns = [
    # myapp/hello/
    path('hello/',views.hello),
    # myapp/bye/
    path('bye/',views.bye),
    # myapp/review/
    path('review/',views.review),

    path('index/',views.index),
    
]

