from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken import views
from .import views

router = DefaultRouter()
router.register(r'employees',views.EmployeeViewSet)
router.register(r'department',views.DepartmentViewSet)

urlpatterns = [
    path("login/",views.LoginAPIView.as_view(),name="user-login"),
   path('user/<int:id>/',views.UserDetailView.as_view(), name='user-detail'),
]