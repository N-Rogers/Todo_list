from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:event_id>', views.del_event, name='delete'),
    path('crossoff/<int:id>', views.cross_off, name='crossoff'),
    path('uncross/<int:id>', views.uncross, name='uncross'),
    path('about/', views.about, name='about'),

]
