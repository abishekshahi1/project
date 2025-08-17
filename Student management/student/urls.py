from django.urls import path
from .views import create_student, update_student, student_list, delete_student, thank_you

urlpatterns = [
    path('', create_student, name="home"),  # 🚀 Redirect '/' to the form page
    path('create/', create_student, name="create"),
    path('update/<int:pk>/', update_student, name="update"),
    path('delete/<int:pk>/', delete_student, name="delete"),
    path('list/', student_list, name="list"),  # list is now available at /list/
    path('thank-you/', thank_you, name="thank_you"),
]
