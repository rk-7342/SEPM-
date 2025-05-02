🎓 Career Guidance System – Project Overview
The Career Guidance System is a web-based platform designed to provide personalized career recommendations for different user categories based on their educational background, interests, test scores, and goals. The system caters to:

Students (10th, 12th, B.Tech, M.Tech)

Entrepreneurs

Career Changers

Employers

Parents

Counselors

Built using Django (Python) as the backend and HTML/CSS/JavaScript for the frontend, the system includes login/signup, dashboard, data entry, career tests (planned), and smart recommendations.

✅ Main Functional Modules
1. 🔐 User Authentication
Signup/Login for all users.

User category selection on signup (student, entrepreneur, etc.).

Category-based redirection after login.

Fields collected at signup: name, email, phone, DOB, password, category.

2. 🎓 Student Module
Sub-categorization by level: 10th, 12th, B.Tech, M.Tech.

Marks Collection:

10th: Subject-wise test reports only.

12th: English, Maths, Science, Social.

B.Tech/M.Tech: Semester-wise subject marks (Sem 1 to Sem 6).

Career Recommendations:

Based on marks and test scores.

Includes career name, reason, roadmap, courses, skills, salary, and institutions.

3. 💼 Entrepreneur Module
Data collected:

Academic info (10th/12th marks).

Hobbies and career interests.

Investment capacity.

Recommendations based on:

Interests (tech, design, cooking, etc.).

Budget.

Potential businesses (freelancing, startups, food business, etc.).

Skills to develop, platforms to use.

4. 🔄 Career Changer Module
Collected:

12th and Degree marks.

Previous skills (coding, marketing, finance, etc.).

Career interests.

Recommendations based on:

Transferable skills.

Interests.

Education level.

Output:

Career fit explanation.

Step-by-step roadmap.

Courses to pursue.

Project ideas.

Salary ranges.

5. 🏢 Employer Module
Collected:

Company name, designation, industry type.

Location, recruitment focus, budget per candidate.

Recommendations:

Where and whom to recruit (top institutions).

Skillsets to target.

Budget suggestions.

Useful hiring platforms/resources.

6. 👨‍👩‍👧 Parent & Counselor Modules (Planned)
Track student progress and reports.

View recommendations.

Provide mentoring/help.

7. 📊 Admin Panel
Manage users, student marks, test results.

Add/update/delete questions for tests.

View data analytics on student performance (planned).

🔧 Planned Features
Test system: Category-specific quizzes (Math, Science, etc.).

Resume builder for students.

Job posting by employers and student applications.

Messaging between students and employers/counselors.

Analytics dashboard for admin.

📦 Tech Stack
Component	Technology
Backend	Django (Python)
Frontend	HTML, CSS, JavaScript
Database	SQLite (default), can migrate to PostgreSQL/MySQL
Authentication	Django User Model
Styling	Custom CSS, gradients
Deployment	Localhost (for now), can be deployed to Heroku, PythonAnywhere, etc.

🎯 Project Outcome
This system helps:

Students choose the right career based on data.

Career changers pivot efficiently.

Entrepreneurs find fitting domains.

Employers match talent with roles.

Parents & counselors stay involved.
