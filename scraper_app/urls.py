from django.urls import path
from .views import Result
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Result.as_view(), name='result'),
]