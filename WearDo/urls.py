from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('WearDo.accounts.urls')),
    path('products/', include('WearDo.products.urls')),
    path('categories/', include('WearDo.categories.urls')),
]
