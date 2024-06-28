"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from amazon import views
from django.contrib.auth import views as auth_views
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.choice_login,name='choice_login'),
    path("owner_admin/",views.owner_admin,name='owner_admin'),
    path("home",views.home,name='home'),
    path("about-us",views.about_us,name='about-us'),
    path("ebook/",views.ebook,name='ebook'),
    path("mobile/",views.mobile,name='mobile'),
    path("clothes/",views.clothes,name='clothes'),
    path("laptops/",views.laptops,name='laptops'),
    path("electronics/",views.electronics,name='electronics'),
    path("shoes/",views.shoes,name='shoes'),
    path("antivirus/",views.antivirus,name='antivirus'),
    path("watches/",views.watches,name='watches'),
    path("monitors/",views.monitors,name='monitors'),
    path("arduino/",views.arduino,name='arduino'),
    path("televisions/",views.televisions,name='televisions'),
    path("mouse/",views.mouse,name='mouse'),
    path("games/",views.games,name='games'),
    path("owner_login/",views.owner_login,name='owner_login'),
    path("hash1290/",views.hash1290,name='hash1290'),
    path("help/",views.help,name='help'),
    path("developer/",views.developer,name='developer'),
    path("feedback/",views.feedback,name='feedback'),
    path("amazon/",views.amazon,name='amazon'),
    path("flipkart2/",views.flipkart2,name='flipkart2'),
    path('documentation/',views.documentation,name='documentation'),
    path("myntra/",views.myntra,name='myntra'),
    path("collaboration/",views.collaboration,name='collaboration'),
    path("about_web/",views.about_web,name='about_web'),
    path("update/",views.update,name='update'),
    path("car/",views.car,name='car'),
    path("bike/",views.bike,name='bike'),
    path("footer/",views.footer,name='footer'),
    path("power_off/",views.power_off,name='power_off'),
    path("user_login/",views.user_login,name='user_login'),
    path("admin_login/",views.admin_login,name='admin_login'),
    path("admin_home/",views.admin_home,name='admin_home'),
    path("admin_credentials/",views.admin_credentials,name='admin_credentials'),
    path("admin_help/",views.admin_help,name='admin_help'),
]
