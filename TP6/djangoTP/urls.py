"""djangoTP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from sim_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.landing, name="landing"),
    path('account/', include('django.contrib.auth.urls')),
    url(r'^profile/', views.edit_profile,name="profile"),
    url(r'^update_password/', views.update_password, name="update_password"),
    url(r'^signup/', views.create_profile, name="signup"),
    url(r'^delete_account/', views.delete_account, name="delete_account"),
    url(r'^sim_list/', views.simulation_list,name="sim_list"),
    url(r'^favorite/', views.add_or_remove_favorite, name="add_or_remove_favorite"),
    url(r'^share/', views.share, name="share"),
    url(r'^disconnect/', views.disconnect, name="disconnect"),
    url(r'^$', views.landing, name="landing"),
    url(r'^newsimu/$', views.new_simu, name='newsimu'),
    url(r'^(?P<object_id>[0-9]+)/run_sim/$', views.run_sim, name='run_sim'),
    url(r'^(?P<object_id>[0-9]+)/delete_sim/$', views.simulation_delete, name='delete_sim'),
]
