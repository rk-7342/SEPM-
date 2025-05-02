from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MarksForm
from .models import StudentMarks, User
from .forms import EntrepreneurSignupForm
from .models import EntrepreneurProfile
from .models import CareerChangerProfile
from .forms import CareerChangerSignupForm



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Redirect entrepreneurs to enter their details before accessing the dashboard
            if user.category == "entrepreneur":
                return redirect('entrepreneur_signup')  # Redirect to entrepreneur details form

            return redirect('dashboard')  # Default redirect for other users
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')


def home(request):
    return render(request, 'users/home.html')

@login_required
def dashboard_view(request):
    if hasattr(request.user, 'category') and request.user.category:  # Ensure category exists
        user_category = request.user.category
    else:
        return render(request, '')  # Handle users without a category

    if user_category == 'student':
        return render(request, 'users/student_dashboard.html')
    elif user_category == 'entrepreneur':
        return render(request, 'users/entrepreneur_dashboard.html')
    elif user_category == 'career_changer':
        return render(request, 'users/career_changer_dashboard.html')
    elif user_category == 'parent':
        return render(request, 'users/parent_dashboard.html')
    elif user_category == 'counsellor':
        return render(request, 'users/counsellor_dashboard.html')
    elif user_category == 'employer':
        return render(request, 'users/employer_dashboard.html')

    # **Fix: No else condition to avoid returning None**


@login_required
def entrepreneur_dashboard_view(request):
    entrepreneur_profile = EntrepreneurProfile.objects.get(user=request.user)

    return render(request, 'users/entrepreneur_dashboard.html', {'entrepreneur': entrepreneur_profile})


@login_required
def student_dashboard_view(request):
    user = request.user  # Get logged-in user

    if hasattr(user, 'education_level') and user.education_level:
        education_level = user.education_level
    else:
        education_level = "Not Provided"

    return render(request, 'users/student_dashboard.html', {'education_level': education_level})

@login_required
def student_marks_view(request):
    user = User.objects.get(id=request.user.id)  # Ensure user is recognized
    student_marks, created = StudentMarks.objects.get_or_create(user=user, education_level=user.education_level)

    if request.method == 'POST':
        form = MarksForm(request.POST, instance=student_marks)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after submission
    else:
        form = MarksForm(instance=student_marks)

    return render(request, 'users/student_marks.html', {'form': form, 'education_level': user.education_level})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import StudentMarks
@login_required
def career_recommendation_view(request):
    student_marks = StudentMarks.objects.get(user=request.user)

    print("Education Level:", student_marks.education_level)
    print("Retrieved Marks: ", student_marks.__dict__)  # Print all marks

    career_data = []  # Store all detailed recommendations

    if student_marks.education_level == "12th":
        if student_marks.maths_12th > 80:
            career_data.append({
                "career": "Engineering (B.Tech in CS, Electronics, Mechanical, etc.)",
                "why": "Engineering is ideal for students with strong analytical and problem-solving skills.",
                "courses": ["B.Tech", "B.E.", "Diploma in Engineering"],
                "skills": ["Mathematics", "Programming", "Problem-Solving"],
                "institutions": ["IITs", "NITs", "SRM University", "BITS Pilani"],
                "exams": ["JEE Main", "JEE Advanced", "State Engineering Exams"],
                "job_roles": ["Software Engineer", "Mechanical Engineer", "Civil Engineer"],
                "salary": "₹6-20 LPA (varies by specialization)",
                "resources": "https://www.nirfindia.org"
            })
        if student_marks.science_12th > 80:
            career_data.append({
                "career": "Medical, Biotechnology, or Research Fields",
                "why": "Ideal for students passionate about healthcare and life sciences.",
                "courses": ["MBBS", "BDS", "B.Sc. Biotechnology"],
                "skills": ["Biology", "Chemistry", "Research"],
                "institutions": ["AIIMS", "CMC Vellore", "JIPMER"],
                "exams": ["NEET", "AIIMS Entrance"],
                "job_roles": ["Doctor", "Biotechnologist", "Research Scientist"],
                "salary": "₹8-30 LPA",
                "resources": "https://www.mciindia.org"
            })

    elif student_marks.education_level in ["btech", "mtech"]:
        if student_marks.sem1_c > 75:
            career_data.append({
                "career": "Software Development, Full Stack Engineer",
                "why": "Ideal for those who enjoy problem-solving and coding.",
                "courses": ["B.Tech in Computer Science", "M.Tech in Software Engineering"],
                "skills": ["C Programming", "Data Structures", "Problem-Solving"],
                "institutions": ["IITs", "NITs", "IIITs", "BITS Pilani"],
                "exams": ["GATE (for M.Tech)", "GRE (for MS)"],
                "job_roles": ["Software Engineer", "Web Developer", "Backend Developer"],
                "salary": "₹8-40 LPA",
                "resources": "https://www.coursera.org"
            })
        if student_marks.sem5_cloud > 75:
            career_data.append({
                "career": "Cloud Computing Specialist",
                "why": "High demand due to increasing cloud-based services.",
                "courses": ["M.Tech in Cloud Computing", "AWS/GCP/Azure Certifications"],
                "skills": ["Cloud Computing", "Networking", "Security"],
                "institutions": ["IIT Bombay", "SRM University", "IISc"],
                "exams": ["AWS Certification", "Microsoft Azure Exam"],
                "job_roles": ["Cloud Engineer", "DevOps Specialist"],
                "salary": "₹10-45 LPA",
                "resources": "https://aws.amazon.com/certification/"
            })

    print("Generated Career Data:", career_data)  # Debugging

    return render(request, 'users/career_recommendation.html', {'career_data': career_data})


def entrepreneur_signup_view(request):
    entrepreneur_profile, created = EntrepreneurProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EntrepreneurSignupForm(request.POST, instance=entrepreneur_profile)
        if form.is_valid():
            form.save()
            return redirect('entrepreneur_recommendation')  # Redirect to recommendations
    else:
        form = EntrepreneurSignupForm(instance=entrepreneur_profile)

    return render(request, 'users/entrepreneur_signup.html', {'form': form})

@login_required
def entrepreneur_recommendation_view(request):
    entrepreneur_profile = EntrepreneurProfile.objects.get(user=request.user)

    recommendations = []

    if entrepreneur_profile.investment_budget < 50000:
        recommendations.append({
            "business": "Freelancing (Coding, Writing, Digital Marketing)",
            "why": "Low investment and high-profit margins. Requires skill development.",
            "skills": ["Coding", "Content Writing", "SEO", "Social Media Marketing"],
            "resources": "https://www.udemy.com"
        })


    if entrepreneur_profile.investment_budget >= 50000 and entrepreneur_profile.investment_budget <= 500000:
        recommendations.append({
            "business": "Small Restaurant, Bakery, or Catering",
            "why": "Ideal for individuals passionate about food & cooking.",
            "skills": ["Culinary Skills", "Marketing", "Customer Service"],
            "resources": "https://www.nrai.org"
        })

    if entrepreneur_profile.investment_budget > 500000:
        recommendations.append({
            "business": "Tech Startup",
            "why": "Great for technology enthusiasts wanting to build a scalable business.",
            "skills": ["App Development", "AI & Machine Learning", "Business Strategy"],
            "resources": "https://www.ycombinator.com"
        })

    return render(request, 'users/entrepreneur_recommendation.html', {'recommendations': recommendations})


@login_required
def career_changer_signup_view(request):
    career_changer_profile, created = CareerChangerProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        print("🚀 Received POST Data:", request.POST)  # ✅ Debugging

        form = CareerChangerSignupForm(request.POST, instance=career_changer_profile)
        if form.is_valid():
            career_profile = form.save(commit=False)  # ✅ Save but don't commit yet

            # ✅ Ensure values are received before saving
            print("✅ Twelfth Marks:", form.cleaned_data.get("twelfth_marks"))
            print("✅ B.Tech/Degree Marks:", form.cleaned_data.get("btech_degree_marks"))
            print("✅ Previous Skills:", request.POST.getlist("previous_skills"))  # Raw skills data
            print("✅ Career Interest:", form.cleaned_data.get("career_preference"))

            # ✅ Convert multiple skills into a string before saving
            career_profile.previous_skills = ', '.join(request.POST.getlist('previous_skills'))
            career_profile.save()  # ✅ Save the object

            print("✅ Successfully Saved Career Changer Profile!")
            return redirect('career_changer_recommendation')  # ✅ Redirect to recommendations page
        else:
            print("❌ Form Errors:", form.errors)  # ✅ Debugging form errors

    else:
        form = CareerChangerSignupForm(instance=career_changer_profile)

    return render(request, 'users/career_changer_signup.html', {'form': form})


@login_required
def career_changer_recommendation_view(request):
    career_changer_profile = CareerChangerProfile.objects.get(user=request.user)

    recommendations = []

    # Debugging Output
    print("Career Changer Profile:")
    print("Education - 12th Marks:", career_changer_profile.twelfth_marks)
    print("Education - B.Tech/Degree Marks:", career_changer_profile.btech_degree_marks)
    print("Previous Skills:", career_changer_profile.previous_skills)
    print("Career Interest:", career_changer_profile.career_preference)

    # ✅ **Technology Career Path**
    if career_changer_profile.career_preference == "technology":
        if career_changer_profile.previous_skills == "coding":
            recommendations.append({
                "new_career": "Data Science & AI",
                "why": "Leverages coding & problem-solving skills for AI-driven applications.",
                "roadmap": [
                    "Step 1: Master Python, SQL, and Data Analysis",
                    "Step 2: Learn Machine Learning & Deep Learning",
                    "Step 3: Work on Real-World AI/ML Projects",
                    "Step 4: Get Certified in AI & Data Science"
                ],
                "courses": ["Python for Data Science", "Machine Learning by Andrew Ng"],
                "projects": ["Build an AI Chatbot", "Create a Stock Market Prediction Model"],
                "institutions": ["IIT Madras", "IIIT Hyderabad", "Google AI"],
                "salary": "₹10-50 LPA",
                "resources": "https://www.coursera.org/specializations/deep-learning"
            })

        if career_changer_profile.previous_skills == "data_analysis":
            recommendations.append({
                "new_career": "Business Intelligence Analyst",
                "why": "Ideal for professionals who enjoy data-driven decision-making.",
                "roadmap": [
                    "Step 1: Learn SQL & Data Visualization (Power BI, Tableau)",
                    "Step 2: Gain expertise in Business Intelligence tools",
                    "Step 3: Work on Market & Sales Forecasting Projects",
                    "Step 4: Get Certified in Business Analytics"
                ],
                "courses": ["Tableau for Beginners", "Power BI Advanced Analytics"],
                "projects": ["Sales Dashboard using Power BI", "Customer Segmentation Analysis"],
                "institutions": ["ISB Hyderabad", "Harvard Business School"],
                "salary": "₹8-30 LPA",
                "resources": "https://www.edx.org/course/business-analytics"
            })

    # ✅ **Business Career Path**
    if career_changer_profile.career_preference == "business":
        if career_changer_profile.previous_skills == "marketing":
            recommendations.append({
                "new_career": "Digital Marketing & Growth Hacking",
                "why": "Expands marketing expertise into high-demand digital fields.",
                "roadmap": [
                    "Step 1: Learn SEO, Google Ads & Social Media Marketing",
                    "Step 2: Build a Marketing Portfolio",
                    "Step 3: Specialize in Growth Hacking Strategies",
                    "Step 4: Get Certified in Google Analytics"
                ],
                "courses": ["Google Digital Marketing Course", "HubSpot SEO Certification"],
                "projects": ["Run a Facebook Ad Campaign", "Analyze Website SEO"],
                "institutions": ["IIM Bangalore", "Harvard Business School"],
                "salary": "₹6-25 LPA",
                "resources": "https://www.udemy.com/course/google-ads-certification"
            })

        if career_changer_profile.previous_skills == "finance":
            recommendations.append({
                "new_career": "Financial Analyst & Investment Banking",
                "why": "Ideal for finance professionals looking to advance in investment roles.",
                "roadmap": [
                    "Step 1: Master Financial Modeling & Valuation",
                    "Step 2: Learn Stock Market & Risk Analysis",
                    "Step 3: Work on Real-World Investment Strategies",
                    "Step 4: Get Certified as a Financial Analyst"
                ],
                "courses": ["Investment Banking by NYIF", "Financial Modeling & Valuation"],
                "projects": ["Create a Stock Portfolio", "Analyze Crypto Investment Trends"],
                "institutions": ["IIM Ahmedabad", "CFA Institute"],
                "salary": "₹12-50 LPA",
                "resources": "https://www.coursera.org/learn/investment-management"
            })

    # ✅ **Creative Field**
    if career_changer_profile.career_preference == "creative":
        if career_changer_profile.previous_skills == "design":
            recommendations.append({
                "new_career": "UI/UX Design",
                "why": "For creative individuals who love user experience & design.",
                "roadmap": [
                    "Step 1: Learn Adobe XD, Figma & Prototyping",
                    "Step 2: Work on Web & Mobile UI Design Projects",
                    "Step 3: Specialize in Human-Centered Design",
                    "Step 4: Get Certified in UX Design"
                ],
                "courses": ["UI/UX Design Specialization", "Adobe XD Masterclass"],
                "projects": ["Redesign an App UX", "Create a Portfolio Website"],
                "institutions": ["NID Ahmedabad", "Parsons School of Design"],
                "salary": "₹7-25 LPA",
                "resources": "https://www.udemy.com/course/ux-design-mastery"
            })

    print("Generated Career Recommendations:", recommendations)

    return render(request, 'users/career_changer_recommendation.html', {'recommendations': recommendations})
