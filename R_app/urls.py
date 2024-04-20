from django.urls import path
from R_app import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('register', views.register, name='REGISTER'),
    path('login', views.login, name='LOGIN'),
    path('display', views.display, name='DISPLAY'),
    path('detail/<str:r_id>', views.detail, name='DETAIL'),
    path('add_recipe', views.add_recipe, name='ADD'),
    path('edit_recipe/<int:r_id>', views.edit_recipe, name='EDIT'),
    path('delete_recipe/<int:r_id>', views.delete_recipe),
    path('logout', views.logout)
]
