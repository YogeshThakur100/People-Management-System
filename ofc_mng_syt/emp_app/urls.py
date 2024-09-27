
from django.urls import path
from . import views
urlpatterns = [
   path('', views.hello , name = 'Hello'),
   path('All_emp', views.All_emp , name = 'All_emp'),
   path('Add_emp', views.Add_emp , name = 'Add_emp') ,
   path('Remove_emp', views.Remove_emp , name = 'Remove_emp'), 
   path('Remove_emp/<int:emp_id>', views.Remove_emp , name = 'Remove_emp'), 
   path('Filter_emp', views.Filter_emp , name = 'Filter_emp'), 
]




   