from django import forms
from .models import  User, Person, Task

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ["name", "email", "mobile"]
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'