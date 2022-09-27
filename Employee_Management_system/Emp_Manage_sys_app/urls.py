from django.urls import path
from Emp_Manage_sys_app import views

urlpatterns=[
    path("",views.index,name='home'),
    path("sign_up/",views.sign_up,name="sign_up"),
    path("all_emp/",views.all_emp,name='all_emp'),
    path("add_emp/",views.add_emp,name='add_emp'),
    path("remove_emp/",views.remove_emp,name='remove_emp'),
    path("filter_emp/",views.filter_emp,name='filter_emp'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path("update_emp/",views.update_emp,name='update_emp'),
    path("update/<int:id>/",views.update,name='update'),
    path("logined/",views.logined,name="logined"),
    path("log_out/",views.log_out,name="log_out")
]