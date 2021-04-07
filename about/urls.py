from django.urls import path
from about import views

urlpatterns = [
    path('create/', views.CreateAboutAPIView.as_view(), name='create'),
    path('list/', views.AboutListAPIView.as_view(), name='list'),
    path('update/<int:pk>', views.AboutUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', views.AboutDeleteAPIView.as_view(), name='delete')
]