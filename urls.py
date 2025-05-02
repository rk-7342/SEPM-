from django.urls import path
from .views import signup_view, login_view, home , dashboard_view,student_marks_view,career_recommendation_view, entrepreneur_signup_view, entrepreneur_recommendation_view, career_changer_signup_view, career_changer_recommendation_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('enter-marks/', student_marks_view, name='enter_marks'),
    path('enter-marks/', student_marks_view, name='enter_marks'),
    path('recommendation/', career_recommendation_view, name='recommendation'),
    path('signup/', signup_view, name='signup'),
    path('entrepreneur-signup/', entrepreneur_signup_view, name='entrepreneur_signup'),
    path('entrepreneur-recommendation/', entrepreneur_recommendation_view, name='entrepreneur_recommendation'),
    path('career-changer-signup/', career_changer_signup_view, name='career_changer_signup'),
    path('career-changer-recommendation/', career_changer_recommendation_view, name='career_changer_recommendation'),

]
