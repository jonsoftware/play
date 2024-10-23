from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todos.models import Todo


class TodosListView(ListView):
    model = Todo


class TodosCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodosUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodosDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
