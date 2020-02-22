from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.camp_list, name ='camp_list'),
    path('camp/<int:pk>', views.camp_detail, name='camp_detail'),
    path('camp/new', views.camp_create, name = 'camp_create'),
    path('review/<int:pk>', views.review_detail, name='review_detail'),
    path('review/new/<int:pk>', views.review_create, name = 'review_create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
