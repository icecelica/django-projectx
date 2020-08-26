from django.contrib import admin
from django.urls import path
from projectx_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('',include('projectx_app.urls')),
    path('projectx_app/',include('projectx_app.urls')),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
]
