from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["project"]
        labels = {
            "user_name": "Numele tău",
            "user_email": "Adresa ta de email",
            "text": "Comentariul tău",
        }