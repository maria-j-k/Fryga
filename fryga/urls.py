from django.contrib import admin
from django.urls import include, path
from exercises import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('exercises/', include('exercises.urls')),
]
