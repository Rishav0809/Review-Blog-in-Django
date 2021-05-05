"""productreview URL Configuration

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
from django.contrib import admin
from django.urls import path
from review import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #Authentication
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('review/<int:review_pk>', views.review, name='review'),    
    path('profile/<int:profile_pk>', views.profile, name='profile'),    

    #ProductReview
    path('', views.home, name='home'),
    path('userpanel/', views.userpanel, name='userpanel'),
    path('userpanel/expertreviews/', views.expertreviews, name='expertreviews'),
    path('createreview/', views.createreview, name='createreview'),
    
    path('updateprofilephoto/', views.updateprofilephoto, name='updateprofilephoto'),
    path('allexperts/', views.allexperts, name='allexperts'),
    path('allreviews/', views.allreviews, name='allreviews'),
    path('generatecode/', views.generatecode, name='generatecode'),
    path('redeemcode/', views.redeemcode, name='redeemcode'),
    path('editreview/<int:review_pk>', views.editreview, name='editreview'),
    path('update/', views.update, name='update'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
