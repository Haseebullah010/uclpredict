"""navbar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from navbar1 import views
from django.conf.urls import  url

urlpatterns = [

    
    path ('',views.home1,name="HOME"),

    path ('Ansufati/',views.one,name="ONE"),
    path ('cirioimmobile/',views.two,name="two"),
    path ('CristianoRonaldo/',views.three,name="three"),
    path ('ErlingHaaland/',views.four,name="four"),
    path ('Kante/',views.five,name="five"),
    path ('KarimBenzema/',views.six,name="six"),
    path ('Kilianmbappe/',views.seven,name="seven"),
    path ('Leonardobonucci/',views.eight,name="eight"),
    path ('Lewandowski/',views.nine,name="nine"),
    path ('LionelMessi/',views.ten,name="ten"),
    path ('MohamedSalah/',views.eleven,name="eleven"),
    path ('Raheemsterling/',views.twelve,name="twelve"),

    path('ucltopscorer/',views.ucltop,name="UCLTOPSCORER"),

    path('getmethod/',views.getmethod,name="GETMETHOD"),

    path('fixture/',views.fixture,name="FIXTURE"),
    path('results/',views.results,name="RESULTS"),
    path('uclwinner/',views.uclwinner,name="UCLWINNER"),
    
    path('prediction/',views.make_pred,name="MAKEPREDICTION"),
    # path('prediction/',views.make_pred,name="NOMATCH"),
    path('transferrumor/',views.transfer,name="TRANSFERRUMORS"),
    
    path('check_user/',views.check_user,name="check_user"),

    path ('signup/',views.signup,name="SIGNINUP"),
    path('singin/',views.singin,name="SIGNIN"),
    path('take_quiz/',views.take_quiz,name="take_quiz"),
    
    path('user_logout/',views.user_logout,name="USER_LOGOUT"),
    path('top8team/',views.top8,name="TOP8TEAM"),
    path('greatestalltime/',views.greatestall,name="GREATTESTALLTIME"),
    
    path('toppredictors/',views.toppred,name="TOPPREDICTORS"),
    
    path('fifapro11/',views.fifapro,name="FIFAPRO11"),
    
    path('uclwinner/',views.uclwinner,name="UCLWINNER"),
    path('admin/', admin.site.urls),
]
