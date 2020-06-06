from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('membership/',views.mebership, name='membership'),
    path('home/', views.home, name='home'),
    path('home/1/', views.detail2002, name='detail2002'),
    path('home/1/vote/', views.vote2002, name='vote2002'),
    path('home/1/results/', views.results2002, name='results2002'),
    path('home/2/', views.detail2010, name='detail2010'),
    path('home/2/vote/', views.vote2010, name='vote2010'),
    path('home/2/results/', views.results2010, name='results2010'),
    path('home/3/', views.detailnow, name='detailnow'),
    path('home/3/vote/', views.votenow, name='votenow'),
    path('home/3/results/', views.resultsnow, name='resultsnow'),
    path('home/4/', views.indexbest, name='indexbest'),
    path('polls/<int:question_id>/', views.detailbest, name='detailbest'),
    path('polls/<int:question_id>/vote/', views.votebest, name='votebest'),
    path('polls/<int:question_id>//results/', views.resultsbest, name='resultsbest'),
]