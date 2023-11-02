from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_title(self):
        # cleaned_data is the dict returned by form
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Oops!! We only accept notes about Django.')
        return title