from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # path('api/', include('main.urls')),
    # path('api-auth', include('rest_framework.urls'))
]
