from django.conf.urls import url
from projectx_app import views

app_name = 'projectx_app' # means, nanti org cari www.domain.com/apps akan keluar

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^bloglist/$',views.bloglist,name='bloglist'), # yang ni def kat views.py
    url(r'about/',views.form_name_view, name='form_name'),
    url(r'^register/$',views.register,name='register'), # views.py
    url(r'^about/$',views.about,name='about'), # yang ni def kat views.py
    url(r'^empty/$',views.empty,name='empty'), # yang ni def kat views.py
    url(r'^user_login/$',views.user_login,name='user_login'),

]
