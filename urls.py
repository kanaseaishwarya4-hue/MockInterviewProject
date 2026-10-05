from django.contrib import admin
from django.urls import path
from platform_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("interviewers/", views.interviewers, name="interviewers"),

    path(
        "interviewer/profile/<str:interviewer_name>/",
        views.interviewer_profile,
        name="interviewer_profile"
    ),

    path(
        "interviewer/book/<str:interviewer_name>/",
        views.book_session,
        name="book_session"
    ),

    path(
        "interview/setup/<str:interview_type>/",
        views.interview_setup,
        name="interview_setup"
    ),

    path(
        "interview/<str:interview_type>/",
        views.interview,
        name="interview"
    ),

    path(
        "interview/result/",
        views.interview_result,
        name="interview_result"
    ),

    path("sessions/", views.sessions, name="sessions"),

    path("practice/", views.practice, name="practice"),

    path("profile/", views.profile, name="profile"),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),

    path("login/", views.user_login, name="login"),

    path("register/", views.register, name="register"),

    path("logout/", views.user_logout, name="logout"),
]