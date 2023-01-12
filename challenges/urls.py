# import path from django.urls
from django.urls import path
# import views
from . import views
# create urlpatterns list
urlpatterns = [
    path("", views.index, name="index"),  # path to index page
    path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenges, name="month-challenge"),
]
