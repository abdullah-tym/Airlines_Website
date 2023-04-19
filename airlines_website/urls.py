"""ResAutoBus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from Dashboard import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashboard.urls')),
    path('contact/', include('Dashboard.urls')),
    path('home/', include('Dashboard.urls')),
    path('signup/', include('Dashboard.urls')),
    path('login/', include('Dashboard.urls')),
    path('profile/', include('Dashboard.urls')),
    path('account/', include('Dashboard.urls')),
    path('flights/', include('Dashboard.urls')),
    path('reservation/', include('Dashboard.urls')),
    path('ticket/', include('Dashboard.urls')),
    # path('index1/', include('Dashboard.urls')),
    path('index5/', include('Dashboard.urls')),
    path('<int:flight_id>/select_seat/', include('Dashboard.urls')),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)