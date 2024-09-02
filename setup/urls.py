from django.urls import include, path
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from carford import views

router = DefaultRouter()
router.register(r'owners', views.OwnerViewSet, basename='owners')
router.register(r'cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('prospect-owners/', views.ProspectOwnerListView.as_view(), name='prospect-owners'),
    path('most-sold-cars/', views.MostSoldCarsView.as_view(), name='most-sold-cars'),
]
