from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name='main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('scoring-list/', views.ScoringListView.as_view(), name="scoring_list"),
    path('scoring-update/<int:pk>/', views.ScoringUpdateView.as_view(), name="scoring_update"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
    path('examination/<int:pk>/', csrf_exempt(views.ExamView.as_view()), name="examination")
]