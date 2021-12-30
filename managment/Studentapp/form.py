from django import forms
from .models import Register, User,dashboard


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class UserRegister(forms.ModelForm):
    role1 = [('student', 'student'), ('teacher', 'teacher'), ('admin', 'admin')]
    role = forms.ChoiceField(widget=forms.RadioSelect(), choices=role1)

    class Meta:
        model = Register
        fields = ['number']


class imgform(forms.ModelForm):
    class Meta:
        model = dashboard
        fields = '__all__'
