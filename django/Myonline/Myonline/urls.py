"""Myonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.static import serve
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter



from Myonline.settings import MEDIA_ROOT
import xadmin
from goods.views import CategoryViewset,TestViewset

router = DefaultRouter()
#配置goods的url
router.register(r'categorys', CategoryViewset, base_name="category")
router.register(r'test', TestViewset, base_name="test")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', include_docs_urls(title="慕学生鲜")),
    path(r'', include(router.urls)),

]
