"""Interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


# InterfaceTestingMock.urls.py
from django.contrib import admin
from django.urls import path
from interface_crud.views import add_article, modify_article, query_article, user_auth, get_token, delete_article

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('articles/', add_article),
#     path('articles', modify_article)
# ]



from  interface_crud.views import add_article,modify_article

urlpatterns = [

    path('admin/', admin.site.urls),
    path("auth/", get_token),

    path('articles/', add_article),
    path('query/', query_article),

    path('articles/<int:article_id>', modify_article),
    path('del_articles/<int:article_id>', delete_article)

]
