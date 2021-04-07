from django.urls import path
from home import views

urlpatterns = [
    path('create/', views.CreateHomeAPIView.as_view(), name='create'),
    path('list/', views.HomeListAPIView.as_view(), name='list'),
    path('update/<int:pk>', views.HomeUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', views.HomeDeleteAPIView.as_view(), name='delete')
]