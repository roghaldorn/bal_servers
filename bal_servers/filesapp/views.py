from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from .models import File
from .forms import FileUploadForm
from django.http import FileResponse


class FileIndexView(ListView):
    model = File
    template_name = 'filesapp/file_index.html'
    context_object_name = 'files'
    extra_context = {'title': 'Файлы'}
    paginate_by = 5
    """
    template_name = 'filesapp/file_index.html'
    extra_context = {'title': 'Файлы'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = File.objects.all()
        return context
    """


class FileDownloadView(TemplateView):
    def get(self, request, file_id, *args, **kwargs):
        file = get_object_or_404(File, pk=file_id)
        response = FileResponse(file.file, as_attachment=True)
        return response


class FileDeleteView(TemplateView):
    def get(self, request, file_id, *args, **kwargs):
        file = get_object_or_404(File, pk=file_id)
        response = FileResponse(file.file, as_attachment=True)
        return response


class FileUploadView(LoginRequiredMixin, FormView):
    form_class = FileUploadForm
    template_name = 'filesapp/file_upload.html'
    success_url = reverse_lazy('file_index')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
