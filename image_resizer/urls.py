from django.urls import path
from .views import *

urlpatterns = [
    path('image-resizer/', ImageResizerList.as_view()),

]
