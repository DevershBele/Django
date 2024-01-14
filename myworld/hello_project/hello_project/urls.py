from django.contrib import admin
from django.urls import path
import hello_app.views as gg



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', gg.hello_world, name='hello_world'),
     path('anime/', gg.anime_waifu, name='anime_waifu'),
     path('date/', gg.current_datetime),
     path('time_after_10_hours/<int:hours>/', gg.time_after_10_hours, name='time_after_10_hours'),
            path('hellodeversh/', gg.hello, name='hello'),
            path('books/', gg.book_list, name='book_list'),

            path('emp', gg.emp),  
    path('show',gg.show),  
    path('edit/<int:id>', gg.edit),  
    path('update/<int:id>', gg.update),  
    path('delete/<int:id>', gg.destroy),  


]
