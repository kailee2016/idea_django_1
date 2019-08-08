from django.urls import path,include
from . import views
app_name="book"
urlpatterns = [
    path('',views.index,name='bookIndex'),
    path('book_detail/<book_id>/',views.book_detail,name='bookDetail')
]