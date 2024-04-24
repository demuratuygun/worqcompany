from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form_view),
    path('step2/<int:owner>/', views.platform_form_view, name="step2"),
    path('complete/', views.complete_view, name="complete")

]