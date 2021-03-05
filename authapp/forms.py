from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authapp.models import User
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password'].label = 'Пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес электронной почты'
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if len(name) == 0:
            # для проверки работоспособности
            print('Не задано имя')
            raise ValidationError('Введите ваше имя!')
        return name
