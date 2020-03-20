from django import forms

class Send(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email