#LoginForm
#SignUp Form
#Profile

from django import forms

from django.contrib.auth.models import User

from Login_SignUp.models import SecurityQuestion

from MainPage.models import EventCategory


class signupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': None,
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }


class loginForm(forms.Form):
    loginUserName = forms.CharField(max_length=50, label="Username")
    loginPassword = forms.CharField(widget=forms.PasswordInput(), label="Password")


class profileForm(forms.Form):
    userFirstName = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={'class': 'myProfileAttr'}))
    userLastName = forms.CharField(max_length=50, label="Last Name")
    userCity = forms.CharField(max_length=50, label="City")
    userCountry = forms.CharField(max_length=50, label="Country")
    userEventInterested = forms.ModelChoiceField(
        queryset=EventCategory.objects.all(),
        label='Events Interested',
        widget= forms.Select(attrs={'style': 'width:95%; height:35px; border: 1px solid #ccc;border-radius: 4px;'})
    )
    userProfileImage = forms.ImageField(required=False,
                                        label='Profile Image',
                                        widget=forms.ClearableFileInput())


class PasswordChangeForm(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-group'}), label="Old Password")
    newPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-group'}), label="New Password")
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-group'}), label="Confirm Password")


class ResetPasswordForm(forms.Form):
    userName = forms.CharField(max_length=50, label="Username")


class ResetPasswordNextForm(forms.Form):
    userName = forms.CharField(max_length=50, label="Username")
    newPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-group'}), label="New Password")
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-group'}), label="Confirm Password")
    answer = forms.CharField(max_length=255, label="Answer")
    question_id = forms.IntegerField(widget=forms.HiddenInput())


class SecurityQuestionForm(forms.Form):
    question1 = forms.ModelChoiceField(queryset=SecurityQuestion.objects.all(), label="Question 1")
    answer1 = forms.CharField(max_length=255, label="Answer 1")
    question2 = forms.ModelChoiceField(queryset=SecurityQuestion.objects.all(), label="Question 2")
    answer2 = forms.CharField(max_length=255, label="Answer 2")
    question3 = forms.ModelChoiceField(queryset=SecurityQuestion.objects.all(), label="Question 3")
    answer3 = forms.CharField(max_length=255, label="Answer 3")