from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives, mail_admins


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Surname')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class CustomSignupForm(SignUpForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='Authors')
        user.groups.add(common_users)

        mail_admins(
            subject='New User!',
            message=f'User <b>{user.username}</b>, registered on site.'
        )

        subject = 'You are welcome on our Call Board!'
        text_content = f'{user.username}, You have successfully registered on the site!'
        html_content = (
            f'<b>{user.username}</b>, You have successfully registered on the'
            f'<a href="http://127.0.0.1:8000/posts/">site</a>'
        )
        msg = EmailMultiAlternatives(
            subject, text_content, to=[user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return user
