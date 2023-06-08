from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
@login_required

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
@login_required
def task_board(request):
    todo_tasks = Task.objects.filter(status='ToDo')
    in_progress_tasks = Task.objects.filter(status='InProgress')
    done_tasks = Task.objects.filter(status='Done')
    return render(request, 'task_board.html', {'todo_tasks': todo_tasks, 'in_progress_tasks': in_progress_tasks, 'done_tasks': done_tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Task.objects.filter(status='todo')
        context['in_progress'] = Task.objects.filter(status='in_progress')
        context['done'] = Task.objects.filter(status='done')
        return context