from django.conf.urls import url, include

from app.views import UserView

urlpatterns = [
    url('^$', UserView.as_view(), name="users")
]
