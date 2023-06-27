from django.urls import path #("/", .as_view(), name="")
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     # ex: /projects/5/
     path("<int:project_id>/", views.detail, name="detail"),
]
