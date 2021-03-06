"""miPrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from miPrimerProyecto.views import get_image, hello_json, hello_world, load_city_list, load_image_by_id, load_image_by_id2, test, time
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('time/', time),
    path('hello-json/', hello_json),
    path('image/', get_image),
    path('image/<str:city_id>', load_image_by_id),
    path('template-test/<str:city_id>', load_image_by_id2),
    path('cities-list/', load_city_list),
    path('template-base-test/', test)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
