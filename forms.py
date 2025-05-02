from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EntrepreneurProfile , CareerChangerProfile, StudentMarks , User

class SignupForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ChoiceField(choices=User.CATEGORY_CHOICES, required=True)
    education_level = forms.ChoiceField(
        choices=User.EDUCATION_LEVEL_CHOICES, required=False
    )  # Only show if "Student" is selected

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'dob', 'category', 'education_level', 'password1', 'password2']

class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = [
            'english_12th', 'maths_12th', 'science_12th', 'social_12th',
            'sem1_c', 'sem2_oodp', 'sem3_os', 'sem3_dsa', 'sem3_app', 'sem3_coa',
            'sem4_daa', 'sem4_dbms', 'sem5_cn', 'sem5_automata', 'sem5_cloud',
            'sem6_compiler', 'sem6_data_science'
        ]

class EntrepreneurSignupForm(forms.ModelForm):
    class Meta:
        model = EntrepreneurProfile
        fields = ['tenth_marks', 'twelfth_marks', 'hobbies', 'career_interest', 'investment_budget']

from django import forms

class CareerChangerSignupForm(forms.ModelForm):
    previous_skills = forms.MultipleChoiceField(
        choices=CareerChangerProfile.SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple,  # ✅ Allows multiple selections
        required=False
    )

    class Meta:
        model = CareerChangerProfile
        fields = ['twelfth_marks', 'btech_degree_marks', 'previous_skills', 'career_preference']

    def clean_previous_skills(self):
        skills = self.cleaned_data.get('previous_skills')
        return ', '.join(skills)  # ✅ Convert to comma-separated string










