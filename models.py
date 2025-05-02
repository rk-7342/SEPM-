from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('entrepreneur', 'Entrepreneur'),
        ('career_changer', 'Career Changer'),
        ('parent', 'Parent'),
        ('counsellor', 'Counsellor'),
        ('employer', 'Employer'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('12th', '12th Class'),
        ('btech', 'B.Tech/Degree'),
        ('mtech', 'M.Tech'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    education_level = models.CharField(
        max_length=10, choices=EDUCATION_LEVEL_CHOICES, blank=True, null=True
    )  # Only for students

    def __str__(self):
        return self.username

class StudentMarks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=10)

    # 12th Class
    english_12th = models.FloatField(default=0)  # Added default=0
    maths_12th = models.FloatField(default=0)
    science_12th = models.FloatField(default=0)
    social_12th = models.FloatField(default=0)

    # B.Tech/M.Tech Semester-wise
    sem1_c = models.FloatField(default=0)
    sem2_oodp = models.FloatField(default=0)
    sem3_os = models.FloatField(default=0)
    sem3_dsa = models.FloatField(default=0)
    sem3_app = models.FloatField(default=0)
    sem3_coa = models.FloatField(default=0)
    sem4_daa = models.FloatField(default=0)
    sem4_dbms = models.FloatField(default=0)
    sem5_cn = models.FloatField(default=0)
    sem5_automata = models.FloatField(default=0)
    sem5_cloud = models.FloatField(default=0)
    sem6_compiler = models.FloatField(default=0)
    sem6_data_science = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.education_level}"


class EntrepreneurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Academic Information
    tenth_marks = models.FloatField(null=True, blank=True)
    twelfth_marks = models.FloatField(null=True, blank=True)

    # Interests
    HOBBY_CHOICES = [
        ('coding', 'Coding'), ('painting', 'Painting'), ('sports', 'Sports'),
        ('writing', 'Writing'), ('cooking', 'Cooking'), ('movies', 'Watching Movies')
    ]
    CAREER_INTERESTS = [
        ('technology', 'Technology'), ('healthcare', 'Healthcare'),
        ('design', 'Design'), ('cooking', 'Cooking')
    ]

    hobbies = models.CharField(max_length=50, choices=HOBBY_CHOICES, blank=True)
    career_interest = models.CharField(max_length=50, choices=CAREER_INTERESTS, blank=True)

    # Investment
    investment_budget = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Entrepreneur: {self.user.username}"

class CareerChangerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Education Background
    twelfth_marks = models.FloatField(null=True, blank=True)
    btech_degree_marks = models.FloatField(null=True, blank=True)

    # Previous Skills (Multi-choice)
    SKILL_CHOICES = [
        ('coding', 'Coding'), ('data_analysis', 'Data Analysis'), ('marketing', 'Marketing'),
        ('finance', 'Finance'), ('design', 'Design'), ('project_management', 'Project Management')
    ]
    previous_skills = models.CharField(max_length=50, choices=SKILL_CHOICES, blank=True)

    # Interests
    CAREER_PREFERENCES = [
        ('technology', 'Technology'), ('business', 'Business'),
        ('creative', 'Creative Field'), ('finance', 'Finance & Investment')
    ]
    career_preference = models.CharField(max_length=50, choices=CAREER_PREFERENCES, blank=True)

    def __str__(self):
        return f"Career Changer: {self.user.username}"



