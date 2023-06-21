from django.urls import include, path
from .views import home, buy_item

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/', buy_item)
]