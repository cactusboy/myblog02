from django.urls import path
from . import views

# 如果你忘了在 blog\urls.py 中添加app_name='blog'这一句，接下来你可能会得到一个 NoMatchReversed 异常
app_name = 'blog'
urlpatterns = [
    # path(r'', views.index, name='index'), 原来的主页视图
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path(r'archives/<int:year>{4})/<int:month>{1,2})/', views.ArchivesView.as_view(), name='archives'),
    path(r'category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path(r'tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path(r'sponsor/', views.sponsor, name='sponsor'),
    path(r'resume/', views.resume, name='resume'),

    # 自带的搜索---
    path(r'search/', views.search, name='search'),
    # 搜索end---

]
'''原教程里的代码
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'post/(?p<pk>[0-9]+)/$', views.detail, name='detail'),
    path(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    path(r'category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
'''
