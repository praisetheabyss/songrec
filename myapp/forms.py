from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


# Create your forms here.

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'birth_date')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = ""
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['birth_date'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""

        self.fields['first_name'].widget.attrs['class'] = 'rounded-5 ps-3 border-0 w-100'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Digite seu primeiro nome'
        self.fields['first_name'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'

        self.fields['last_name'].widget.attrs['class'] = 'rounded-5 ps-3 border-0 w-100'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Digite seu sobrenome'
        self.fields['last_name'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'

        self.fields['username'].widget.attrs['class'] = 'rounded-5 ps-3 border-0'
        self.fields['username'].widget.attrs['placeholder'] = 'Digite seu username'
        self.fields['username'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'

        self.fields['email'].widget.attrs['class'] = 'rounded-5 ps-3 border-0'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu e-mail'
        self.fields['email'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'

        self.fields['password1'].widget.attrs['class'] = 'rounded-5 ps-3 border-0 w-100'
        self.fields['password1'].widget.attrs['placeholder'] = 'Digite sua senha'
        self.fields['password1'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'


        self.fields['password2'].widget.attrs['class'] = 'rounded-5 ps-3 border-0 mb-3 w-100'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
        self.fields['password2'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'

        self.fields['birth_date'].widget.attrs['class'] = 'rounded-5 ps-3 border-0'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'DD/MM/YY'
        self.fields['birth_date'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'
        self.fields['birth_date'].widget.attrs['type'] = 'date'

class CustomLoginForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-class'})
        }


    # def __init__(self, *args, **kwargs):
    #     super(CustomLoginForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].label = ""
    #     self.fields['password'].label = ""

    #     self.fields['username'].widget.attrs['class'] = 'rounded-5 ps-3 border-0 w-100'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Digite seu primeiro nome'
    #     self.fields['username'].widget.attrs['style'] = 'background: #403D3D; color: #909090; height: 50px;'



