
from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner-page/', views.innerpage,name='inner-page'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path ('Detail/',views.Details,name='Details'),
    path ('users/',views.users,name='users'),
    path ('adminhome/',views.adminhome,name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
