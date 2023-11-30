from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    email = forms.EmailField(label='E-Mail Address')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = \
        'name'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
        'email'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
        'message'
        self.fields['message'].widget.attrs['class'] = 'form-control'