from django.forms import ModelForm
from .models import JobAdvert, JobApplication
from django import forms



class JobAdvertForm(ModelForm):
    class Meta:
        model = JobAdvert
        fields = [
            "title",
            "company_name",
            "employment_type",
            "experience_level",
            "job_type",
            "location",
            "description",
            "skills",
            "is_published",
            "deadline"
        ]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder":"Job title", "class":"form-control"}),
            "description": forms.Textarea(attrs={"placeholder":"Description", "class":"form-control"}),
            "company_name": forms.TextInput(attrs={"placeholder":"Company name", "class":"form-control"}),
            "employment_type": forms.Select(attrs={"class":"form-control"}),
            "experience_level": forms.Select(attrs={"class":"form-control"}),
            "job_type": forms.Select(attrs={"class":"form-control"}),
            "location": forms.TextInput(attrs={"placeholder":"Optional", "class":"form-control"}),
            "deadline": forms.DateInput(attrs={"placeholder":"Date", "class":"form-control", "type":"date"}),
            "skills": forms.TextInput(attrs={"placeholder":"Comma separated skills", "class":"form-control"}),

        }


class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "name",
            "email",
            "portfolio_url",
            "cv"
        ]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class":"form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email", "class":"form-control"}),
            "portfolio_url": forms.URLInput(attrs={"placeholder": "Portfolio link", "class":"form-control"}),
            "cv": forms.FileInput(attrs={"placeholder": "Select your cv", "class":"form-control", "accept":".pdf, .docx, .doc"}),
        }
