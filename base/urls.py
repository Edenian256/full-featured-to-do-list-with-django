from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views
from .views import contact
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'base/password_reset_form.html', 
    subject_template_name = 'base/password_reset_subject_txt',
    email_template_name = 'base/password_reset_email.html'), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'base/password_reset_done.html'
    ), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'base/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('passwor_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'base/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('change_password', auth_views.PasswordChangeView.as_view(
        template_name =  'base/change_password.html',
        success_url = '/'
    ), name = 'change_password'),
       
]