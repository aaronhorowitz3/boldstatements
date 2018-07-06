from django import forms
from .models import Statement

class MakeAStatement(forms.ModelForm):

    class Meta:
        model = Statement
        fields = ('prediction', 'predictor', 'description', 'image', 'link')
