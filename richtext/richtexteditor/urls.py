from django.urls import path
from .import views

urlpatterns=[
    path('', views.save_form_view , name='rich-text-editor'),
    path('show/', views.show_saved_data, name='show-saved-data'),
]