import csv
import datetime
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.finance.models import Invoice,Receipt,InvoiceItem
from apps.staffs.models import Staff
from .models import Student, StudentBulkUpload
from django.db.models import Sum
import datetime
@login_required()
def index(request):
    ia =Staff.objects.filter(current_status='inactive').count()
    iat =Staff.objects.all().filter(current_status='inactive')
    a=InvoiceItem.objects.aggregate(Sum('amount'))
    bfv=Invoice.objects.aggregate(Sum('balance_from_previous_term'))
    students= Student.objects.all().count()
    staffs = Staff.objects.all().count()
    fees = Receipt.objects.aggregate(Sum('amount_paid'))
    newstu =Student.objects.filter(date_of_admission=datetime.date.today())
    newf =Receipt.objects.filter(date_paid=datetime.date.today())[:50]
    tos=Receipt.objects.filter(date_paid=datetime.date.today()).aggregate(Sum('amount_paid'))
    c =a['amount__sum']+bfv['balance_from_previous_term__sum']
    b=c-fees['amount_paid__sum']
    context= {'stu':students,'sta':staffs,'fee':fees,'ns':newstu,'nf':newf,'ts':tos,'bs':bfv,'as':a,'d':c,'b1':b,'ia':ia,'iat':iat}

    return render(request,"index.html",context)

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "index.html"
    template_name = "students/student_list.html"
    
    students= Student.objects.all()

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["payments"] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    success_message = "New student successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "students/students_upload.html"
    fields = ["csv_file"]
    success_url = "/student/list"
    success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response
