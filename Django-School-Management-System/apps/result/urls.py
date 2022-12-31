from django.urls import path

from .views import ResultListView, create_result, edit_results,GetResultView

urlpatterns = [
    path("create/", create_result, name="create-result"),
    path("edit-results/", edit_results, name="edit-results"),
    path("view/all", ResultListView.as_view(), name="view-results"),
    path("result", GetResultView.as_view(), name="get-results"),
]
