from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    LoginView, RegisterView,
    MainPageView,
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    ClassListView, ClassCreateView, ClassUpdateView, ClassDeleteView
)

from .views import (
    PasswordResetRequestView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView
)

urlpatterns = [

    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', MainPageView.as_view(), name='home'),

    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/add/', TeacherCreateView.as_view(), name='add_teacher'),
    path('teacher/edit/<int:pk>/', TeacherUpdateView.as_view(), name='edit_teacher'),
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher'),
    
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subject/add/', SubjectCreateView.as_view(), name='add_subject'),
    path('subject/edit/<int:pk>/', SubjectUpdateView.as_view(), name='edit_subject'),
    path('subject/delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),
    
    path('students/', StudentListView.as_view(), name='student_list'),
    path('student/add/', StudentCreateView.as_view(), name='add_student'),
    path('student/edit/<int:pk>/', StudentUpdateView.as_view(), name='edit_student'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('class/add/', ClassCreateView.as_view(), name='add_class'),
    path('class/edit/<int:pk>/', ClassUpdateView.as_view(), name='edit_class'),
    path('class/delete/<int:pk>/', ClassDeleteView.as_view(), name='delete_class'),
]