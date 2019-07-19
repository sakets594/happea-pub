
from django.contrib import admin
from django.urls import path,include,reverse_lazy
from .views import home,loginpage,quizes,quizintro,profileinfocheck,redirecttologin,addquiz
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import NewsCreateView,NewsUpdateView,NewsListView,NewsDeleteView,QuizImageCreateView

urlpatterns = [
   
    # path('',home ,name='home'),
    path('',home,name='home'),
    
    path('getstarted/',quizintro ,name='quizintro'),
    path('loginpage/',loginpage , name='loginpage'),
    path('profile/',profileinfocheck , name='profileinfocheck'),
    path('login/',redirecttologin,name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('quizes/', quizes, name='quizes'),
    path('add/',addquiz,name='addQuiz'),
    path('addnews/',NewsCreateView.as_view(),name='newscreate'),
    path('listnews/',NewsListView.as_view(),name='newslist'),
    path('updatenews/<int:pk>/',NewsUpdateView.as_view(),name='newsupdate'),
    path('deletenews/<int:pk>/',NewsDeleteView.as_view(),name='newsdelete'),
    path('addquizimage/',QuizImageCreateView.as_view(),name='addquizimage'),
    
]
