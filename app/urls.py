from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('',views.home,name='home'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    

    path('admin/', views.admin, name='adminpage'),
    
    path('admin/alltasks/', views.all_task, name='alltasks'),
    path('admin/all-client/', views.all_client, name='all_client'),
    path('admin/all-writter/', views.all_writter, name='all_writter'),
    path('admin/view/<int:id>', views.admin_view, name='admin_view'),
    path('admin/approve/user/<int:id>',views.approve,name='approve'),
    path('client/', views.client, name='client'),
    
    path('client/addtask/', views.addtasks, name='addtasks'),
    path('client/all-task/', views.all_task, name='all_task'),
    path('client/delete/<int:id>', views.delete_task, name='delete'),
    path('client/done/jobs/', views.done_task, name='done'),
    path('writter/submit/',views.client_task_update,name='update'),
    path('writter/', views.writter, name='writter'),
    path('writter/view/<int:id>',views.writerForm,name='view'),
    
    path("logout/", views.logout_request, name= "logout"),
    

 


]