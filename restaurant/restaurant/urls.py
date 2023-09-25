from django.contrib import admin
from django.urls import path,include
# importing settings for media folder 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("ourapp.urls")),
    # path('auth/',include("authentication.urls"))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
