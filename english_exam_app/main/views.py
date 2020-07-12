import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from .forms import InquiryForm, DiaryCreateForm
from .models import Diary, Question, Answer

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('main:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        #diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        diaries = Diary.objects.all().order_by('-created_at')
        return diaries

class ScoringListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'scoring_list.html'
    paginate_by = 2

    def get_queryset(self):
        #diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        diaries = Diary.objects.all().order_by('-created_at')
        return diaries

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('main:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('main:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('main:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)

class ExamView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        chapter = Diary.objects.get(id=kwargs['pk'])
        contents = Question.objects.filter(chapter=chapter.id)
        # todo データやりとり実施
        title = chapter.title
        return render(request, 'examination.html', {'questions':contents, "title":title, 'isdone':False })

    def post(self, request, *args, **kwargs):
        logger.debug(request.user)
        logger.debug(request.POST)
        logger.debug(request.FILES)
        logger.debug(args)
        logger.debug(kwargs)

        chapter = Diary.objects.get(id=kwargs['pk'])
        contents = Question.objects.filter(chapter=chapter.id)

        for c in contents:
            ans1 = request.POST['answer_1{0}'.format(c.title)]
            eng = request.POST['english{0}'.format(c.title)]
            ans2 = request.POST['answer_2{0}'.format(c.title)]

            answer = Answer(question=c, user=request.user, answer=ans1, english_translated=eng, answer2 = ans2)
            answer.save()
        return render(request, 'examination.html', {'questions': [], "title": "テストお疲れ様でした！先生のフィードバックを楽しみに待っていていね！", "isdone":True})

class ScoringUpdateView(LoginRequiredMixin, generic.DetailView):
    def get(self, request, *args, **kwargs):
        logger.debug(kwargs)
        chapter = Diary.objects.get(id=kwargs['pk'])
        questions = Question.objects.filter(chapter=chapter.id)
        answers = []
        for q in questions:
            anss = Answer.objects.filter(question=q)
            for ans in anss:
                answers.append(ans)
        return render(request, 'scoring_update.html', {"answers":answers})