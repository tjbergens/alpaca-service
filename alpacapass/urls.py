from rest_framework.authtoken import views
from purplealpaca import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
#router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/register', 'purplealpaca.views.create_auth'),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)