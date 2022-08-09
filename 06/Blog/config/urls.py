from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', RedirectView.as_view(url='blog/')),

    # Blog
    path('', include('blog.urls')),

]
