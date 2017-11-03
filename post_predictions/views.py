from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import Pick
from .forms import CreatePickForm

from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class FullList(TemplateView):
    template_name = "picks/full_list.html"
    
class CreatePick(CreateView):
    model = Pick
    form_class = CreatePickForm
    template_name = "picks/pick_form.html"
    success_url = "picks/pick_list/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PickListView(ListView):
    model = Pick
    template_name = "picks/pick_list.html"

class UserPicksView(ListView):
    model = Pick
    template_name = "picks/user_pick_list.html"
    
class CategoryPicks(ListView):
    model = Pick
    template_name = "picks/category_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return Pick.objects.filter(category=self.kwargs.get("category"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get("category")
        return context


class UpdatePickView(UpdateView):
    model = Pick
    fields = ("prediction", "category")
    template_name = "picks/pick_form.html"
    success_url = "picks/pick_list"

class DeletePickView(DeleteView):
    model = Pick
    template_name = "picks/pick_confirm_delete.html"
    success_url = "picks/pick_list"
