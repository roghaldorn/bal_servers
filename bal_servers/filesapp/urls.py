from django.urls import path
from filesapp.views import FileIndexView, FileUploadView, FileDownloadView, FileDeleteView


urlpatterns = [
    path('', FileIndexView.as_view(), name='file_index'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='download_file'),
    path('delete/<int:file_id>/', FileDeleteView.as_view(), name='delete_file'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
]
