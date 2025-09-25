from django.contrib import admin
from django.urls import path, include
from blog.views import home  # sua view da home

urlpatterns = [
    path('admin/', admin.site.urls),     # rota do admin
    path('blog/', include('blog.urls')), # todas as URLs do blog
    path('', home, name='home'),         # rota raiz ("/")
]
