"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from homepage import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='homepage'),
  #  path(''),
    path('addpost/', views.add_roast_boast),
    path('upvote/<int:post_id>/', views.add_upvote),
    path('downvote/<int:post_id>/', views.add_downvote),
    path('roasts/', views.roasts),
    path('boasts/', views.boasts),
    path('topvotes/', views.top_votes),
    path('admin/', admin.site.urls),
]
