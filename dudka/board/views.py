from datetime import datetime

from django.shortcuts import render, redirect

from .models import Artiles, Answer
from .forms import ArtilesForm
from .forms import AnswerForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
def board(request):
    board = Artiles.objects.order_by('date')
    return render(request, 'board/board.html', {'board': board})

class BoardView(DetailView):
    model = Artiles
    template_name = 'board/view.html'
    context_object_name = 'article'


    def get(self, request, *args, **kwargs):
        answer = Answer.objects.filter(que_id=kwargs.get('pk'))
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['answer'] = answer
        form = AnswerForm()
        context['form'] = form
        # context.view.template_name = 'board/view.html'
        return self.render_to_response(context)

class BoardUpdate(UpdateView):
    model = Artiles
    template_name = 'board/create.html'

    form_class = ArtilesForm

class BoardDelete(DeleteView):
    model = Artiles
    success_url = '/board/'
    template_name = 'board/delete.html'

def answer(request, pk, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.que_id = pk
            new_post.save()
            return redirect(f'/board/{pk}')
        else:
            error = 'Ошибка формы'
    form = AnswerForm()

    data = {
        'form': form
    }
    return render(request, 'board/answer.html', data)

def create(request):
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.date = datetime.now()
            new_post = form.save(commit=False)
            new_post.user = request.user
            form.user = request.user
            new_post.save()
            form.save()
            return redirect('/board')
        else:
            error = 'Ошибка формы'
    form = ArtilesForm()

    data = {
        'form': form
    }
    return render(request, 'board/create.html', data)