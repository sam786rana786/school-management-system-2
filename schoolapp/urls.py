from django.urls import   include,path
from .views import dashboard,principal, students,teachers 
urlpatterns = [
    path('',dashboard.home,name='home'),
    path('principal/', include(([
        path('principal-home',principal.PrincipalHomeView.as_view(),name='principal-home'),
    ], 'dashboard'),namespace='principal')),
     path('student/', include(([
        path('student-home',students.StudentHomeView.as_view(),name='student-home'),
    ], 'dashboard'),namespace='student')),
        path('teacher/', include(([
        path('teacher-home',teachers.TeacherHomeView.as_view(),name='teacher-home'),
    ], 'dashboard'),namespace='teacher')),
    
    ]