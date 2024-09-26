from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    # title = forms.CharField(label="title", max_length=50, required=True)
    # description = forms.CharField(label="description", max_length=200, required=True)

    title = forms.CharField(
        # label="Task Title",
        
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the task title'})
    )
    description = forms.CharField(
        # label="Task Description",
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter a detailed description'})
    )

    class Meta:
        model = Todo
        fields = ['title', 'description']