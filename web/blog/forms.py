from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Escribe tu nombre"}
        ),
    )
    body = forms.CharField(
        max_length= 2000,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Deja un comentario"}
        )
    )