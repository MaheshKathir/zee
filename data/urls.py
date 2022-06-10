from django.urls import path

from data import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('two_list', views.two_list, name='two_list')
]
