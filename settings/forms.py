from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password"]:  # 🔹 Only update password if it's provided
            user.set_password(self.cleaned_data["password"])  # Hash the password
        else:
            user.password = User.objects.get(pk=user.pk).password  # 🔹 Keep the old password
        
        if commit:
            user.save()
        return user
