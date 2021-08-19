from . import views
from django.urls import path 

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('index/',views.index, name = 'index'),
    path('login/', views.login_user, name = 'login_user'),
    path('cadastrar/', views.cadastrar_user, name = 'cadastrar_user'),
    path('deslogar/', views.deslogar_usuario, name='logout'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('create', views.PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'), 
    path('search/results/', views.PostSearch.as_view(), name='search_results'),   
]
