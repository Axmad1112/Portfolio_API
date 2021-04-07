from django.urls import path
from work import views

urlpatterns = [
    path('create/', views.CreateWorkAPIView.as_view(), name='create'),
    path('list/', views.WorkListAPIView.as_view(), name='list'),
    path('update/<int:pk>', views.WorkUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', views.WorkDeleteAPIView.as_view(), name='delete')
]