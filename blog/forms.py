from django import forms
from .models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")

    def clean_message(self):
        message = self.cleaned_data['message']
        if "Nugget" in message:
            raise forms.ValidationError("Nugget est le plus mignion !")

        return message 


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'