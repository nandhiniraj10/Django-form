from django.urls import path
# from . import views
from .views import create_person,success
# from .views import generate_and_view_token

urlpatterns = [
    # path('generate-and-view-token/<int:user_id>/', generate_and_view_token, name='generate_and_view_token'),
    # path('index/', views.index)
    path('create/', create_person, name='create_person'),
    path('success/', success, name='success'),
    
]
