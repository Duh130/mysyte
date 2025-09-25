from django.contrib import admin
from django.urls import path
from blog.views import home, about

from django.contrib import admin
from django.urls import path
from blog.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
]
