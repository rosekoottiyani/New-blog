from django.urls import path,re_path
from . import views

urlpatterns=[
path('',views.index),
path('register/',views.regist),
path('login/',views.login),
path('reset/',views.reset),
path('blog/',views.cblog),
path('vblog/',views.viewBlog),
path('allblog/',views.viewallblogs),
path('logout/',views.logout),
path('vblog/blogid=<int:pk>', views.editBlog,name='editblog'),
path('editblog/',views.update,name='update'),
#re_path(r'(?P<pk>[0-9]+)/$', views.editblog, name='editblog'),
#re_path(r'(?P<pk>[0-9]+)/updateblog/$', views.updateblog, name='updateblog'),
]