from django import forms
from todo.models import Todos


class TodosForm(forms.ModelForm):
    todo = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the Task (Max.100 Characters)',
    }))
    class Meta:
        model = Todos
        fields = ['todo']

        
      