from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.urls import reverse_lazy
from .models import Teacher, Subject, Student, Class
from .forms import TeacherForm, SubjectForm, StudentForm, ClassForm, LoginForm, CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)
    
class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers_count'] = Teacher.objects.count()
        context['students_count'] = Student.objects.count()
        context['subjects_count'] = Subject.objects.count()
        context['classes_count'] = Class.objects.count()
        return context


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = "teacher_list.html"
    context_object_name = "teachers"
    paginate_by = 10
    login_url = 'login'


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_form.html"
    success_url = reverse_lazy('teacher_list')
    login_url = 'login'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_form.html"
    success_url = reverse_lazy('teacher_list')
    login_url = 'login'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = "teacher_confirm_delete.html"
    success_url = reverse_lazy('teacher_list')
    login_url = 'login'


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "subject_list.html"
    context_object_name = "subjects"
    paginate_by = 10
    login_url = 'login'


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject_form.html"
    success_url = reverse_lazy('subject_list')
    login_url = 'login'


class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject_form.html"
    success_url = reverse_lazy('subject_list')
    login_url = 'login'


class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = "subject_confirm_delete.html"
    success_url = reverse_lazy('subject_list')
    login_url = 'login'


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    paginate_by = 10
    login_url = 'login'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')
    login_url = 'login'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')
    login_url = 'login'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy('student_list')
    login_url = 'login'


class ClassListView(LoginRequiredMixin, ListView):
    model = Class
    template_name = "class_list.html"
    context_object_name = "classes"
    paginate_by = 10
    login_url = 'login'


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = "class_form.html"
    success_url = reverse_lazy('class_list')
    login_url = 'login'


class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "class_form.html"
    success_url = reverse_lazy('class_list')
    login_url = 'login'


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = "class_confirm_delete.html"
    success_url = reverse_lazy('class_list')
    login_url = 'login'



from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .forms import PasswordResetRequestForm, SetNewPasswordForm
from django.contrib.auth import get_user_model
from django.shortcuts import render

class PasswordResetRequestView(FormView):
    template_name = 'password_reset_request.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        User = get_user_model()
        user = User.objects.get(email=email)
        
        current_site = get_current_site(self.request)
        subject = 'Відновлення пароля'
        context = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if self.request.is_secure() else 'http',
        }
        message = render_to_string('password_reset_email.html', context)
        
        send_mail(
            subject,
            message,
            'noreply@yourschool.com',
            [email],
            fail_silently=False,
            html_message=message
        )
        
        return super().form_valid(form)

class PasswordResetConfirmView(FormView):
    template_name = 'password_reset_confirm.html'
    form_class = SetNewPasswordForm
    success_url = reverse_lazy('password_reset_complete')

    def dispatch(self, request, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(kwargs['uidb64']))
            user = get_user_model().objects.get(pk=uid)
            
            if not default_token_generator.check_token(user, kwargs['token']):
                return self.invalid_token()
                
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return self.invalid_token()
            
        self.user = user
        return super().dispatch(request, *args, **kwargs)

    def invalid_token(self):
        return render(self.request, 'password_reset_invalid.html')

    def form_valid(self, form):
        self.user.set_password(form.cleaned_data['new_password1'])
        self.user.save()
        return super().form_valid(form)

class PasswordResetDoneView(TemplateView):
    template_name = 'password_reset_done.html'

class PasswordResetCompleteView(TemplateView):
    template_name = 'password_reset_complete.html'