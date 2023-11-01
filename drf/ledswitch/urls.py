from django.urls import path
from .views import LedSTATEView

urlpatterns = [
    path('switch/', LedSTATEView.as_view({
        'post':'switchstate',
        'get':'switchstateget'
    }))
]