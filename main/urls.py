from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_reg_page),
    path('create_user', views.create_user),
    path('login',views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard_page),
    path('add', views.add_job_page),
    path('create', views.create_job),
    path('jobs/<int:job_id>/edit', views.edit_job_page),
    path('jobs/<int:job_id>/update', views.update_job),
    path('jobs/<int:job_id>', views.view_job_page),
    path('jobs/<int:job_id>/add_to_user', views.add_job_to_user),
    path('jobs/<int:job_id>/done', views.done_job),
    path('jobs/<int:job_id>/delete', views.delete_job),
    path('jobs/<int:job_id>/remove_from_user', views.remove_job_from_user),
]