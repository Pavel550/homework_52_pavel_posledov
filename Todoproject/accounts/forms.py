from django.contrib.auth.models import User
from django import forms


class ProjectUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)
    first_name = forms.CharField(label="Фамилия",required=False, strip=False)
    last_name = forms.CharField(label="Имя", required=False, strip=False)
    email = forms.EmailField(max_length=100, required=True)



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not first_name and not last_name:
            raise forms.ValidationError('Хотя бы одно из полей: (first_name,last_name) должно быть заполнено')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
