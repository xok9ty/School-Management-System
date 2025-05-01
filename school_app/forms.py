from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Class, Student, Subject, Teacher
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['num_class', 'name_class', 'head_teacher', 'student']
        widgets = {
            'num_class': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер класу'
            }),
            'name_class': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву класу'
            }),
            'head_teacher': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ПІБ класного керівника'
            }),
            'student': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'num_class': 'Номер класу',
            'name_class': 'Назва класу',
            'head_teacher': 'Класний керівник',
            'student': 'Учні',
        }
        help_texts = {
            'num_class': 'Наприклад: 5, 9-А тощо',
            'name_class': 'Повна назва класу',
            'student': 'Оберіть учнів зі списку',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім\'я'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть прізвище'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть телефон'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'home_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть адресу'
            }),
            'class_num': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'subject_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву предмету'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис предмету',
                'rows': 3
            }),
            'num_classs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть кількість уроків'
            }),
            'teacher': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім\'я'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть прізвище'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть телефон'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'email': 'Email',
            'phone': 'Телефон',
            'birthday': 'Дата народження',
        }
        help_texts = {
            'phone': 'Формат: +380XXXXXXXXX',
        }

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть ваш email'
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Користувача з таким email не знайдено")
        return email

class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label='Новий пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть новий пароль'
        })
    )
    new_password2 = forms.CharField(
        label='Підтвердіть пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Підтвердіть новий пароль'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Паролі не співпадають")
        return cleaned_data
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть ваш email'
        }),
        required=True
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна адреса вже використовується.")
        return email