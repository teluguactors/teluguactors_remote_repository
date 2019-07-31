from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'

            }
        )
    )
    rating = forms.IntegerField(
        label="enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your rating(between 1 to 5)'

            }
        )
    )
    feedback = forms.CharField(
        label="enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your feedback'

            }
        )
    )
class ContactForm(forms.Form):

    name = forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'

            }
        )
    )
    location = forms.CharField(
        label="enter your location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your location'

            }
        )
    )
    salary = forms.IntegerField(
        label="enter your salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your salary'

            }
        )
    )
    email = forms.EmailField(
        label="enter your email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'

            }
        )
    )