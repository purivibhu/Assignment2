from django import forms
from django.core.exceptions import ValidationError
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'enrollment_date', 'grade', 'email', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Date picker for date_of_birth
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),  # Date picker for enrollment_date
        }

    # Custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Optional: You can add custom validation here if needed, or leave it to Django's default.
        return email
    
    
    # Custom validation for the grade field
    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade < 1 or grade > 12:
            raise ValidationError('Grade must be between 1 and 12.')
        return grade
