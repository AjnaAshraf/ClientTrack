from django.urls import path
from leads.views import LeadCreateView,LeadListView
from leads.views import LeadRetrieveViewUpdateDelete

urlpatterns=[

    path("add/",LeadCreateView.as_view()),
    path("list/",LeadListView.as_view()),
    path("modify/<int:pk>/",LeadRetrieveViewUpdateDelete.as_view()),
]