from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name='home'),
    path('play/<int:play_id>', views.play, name='play'),
    path('list/<int:play_id>', views.list, name='list'),
    path('play/<int:play_id>/<int:part_id>/', views.play_list, name='play_list'),
    path('search/', views.search , name='search'),
    path('category/thai_movies', views.thai_movie_category , name='thai_movie_category'),
    path('category/eng_movies', views.eng_movie_category , name='eng_movie_category'),
    path('category/korea_series', views.korea_series_category , name='korea_series_category'),
    path('category/eng_series', views.eng_series_category , name='eng_series_category'),
    path('category/cartoons', views.cartoon_category , name='cartoon_category'),
    
]
