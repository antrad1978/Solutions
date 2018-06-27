"""support_console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from licensing.models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = License
        fields = ('machine_id',)

# ViewSets define the view behavior.
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.filter(machine_id__isnull=True)
    serializer_class = LicenseSerializer

    def get_queryset(self):
        queryset = License.objects.all()
        machine_id = self.request.query_params.get('machine_id', None)
        if machine_id is not None:
            queryset = queryset.filter(machine_id=machine_id)
        else:
            queryset = License.objects.filter(machine_id__isnull=True)
        return queryset

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'license', LicenseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
