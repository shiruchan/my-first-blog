from django.urls import path
from . import views

urlpatterns = [
    # 以下コメント
    # クライアントがアクセスしてきたURLのドメイン以降に何も指定されていないのであれば、処理をviews.pyのpost_listオブジェクトに渡す。
    # nameで指定した"post_list"を指定しておく事で、テンプレートからこの名前でリンクを張ったりする事ができる。
    path('', views.post_list, name='post_list'),
    # URLのドメイン以降でpost/[数字]が付いていれば、views.pyのpost_detailに処理を渡す。末尾の数字はpost_detailの引数(int型)として扱われる
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
