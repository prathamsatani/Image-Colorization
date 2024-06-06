from django import forms


class MyForm(forms.Form):
    image = forms.ImageField(
        allow_empty_file=True, 
        required=False, 
        label="Upload Image",
        error_messages={},
    )
