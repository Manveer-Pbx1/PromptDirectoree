from django.urls import path
from .views import PromptListCreateView, PromptDetailsView

urlpatterns = [
    path('prompts', PromptListCreateView.as_view(), name='prompt-list'),
    path('prompts/<str:id>', PromptDetailsView.as_view(), name='prompt-details'),
]