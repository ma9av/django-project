"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

from accounts.models import Account
from crm.views import CRUDViewSet
from leads.models import Lead
from opportunities.models import Opportunity

lead_crud = CRUDViewSet()
lead_crud.model = Lead

account_crud = CRUDViewSet()
account_crud.model = Account

opportunity_crud = CRUDViewSet()
opportunity_crud.model = Opportunity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include((lead_crud.get_urls(),'leads'),'leads')),
    path('accounts/', include((account_crud.get_urls(),'accounts'),'accounts')),
    path('opportunities/', include((opportunity_crud.get_urls(),'opportunities'),'opportunities')),
    path('api/auth/', include('users.urls')),
    path('api/', include('leads.urls')),
    path('api/', include('opportunities.urls')),

]
