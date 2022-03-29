from django.urls import path
from helloapp.views import HelloWorldView, HelloView, GoodByeView, GoodByeNameView

urlpatterns = [
    # hello/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>/', HelloView.as_view(), name='hello_name'),
    path('goodbye/django/', GoodByeView.as_view(), name='goodbye'),
    path('goodbye/<name>/', GoodByeNameView.as_view(), name='goodbye_name'),
]
