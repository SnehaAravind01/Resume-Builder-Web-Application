from django import forms

class ResumeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    mobile = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    email = forms.EmailField(required=True)
    skills = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    # Educational Details
    education_type = forms.CharField(max_length=50, required=False)
    board = forms.CharField(max_length=100, required=False)
    marks_type = forms.ChoiceField(choices=[("Percentage", "Percentage"), ("CGPA", "CGPA")], required=False)
    marks = forms.CharField(max_length=10, required=False)

    # Work Experience
    company_name = forms.CharField(max_length=100, required=False)
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    # Certifications and Achievements
    certification = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
