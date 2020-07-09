from accounts.models import CustomUser
from django.db import models

class TextBook(models.Model):
    """教科書モデル"""
    title = models.CharField(verbose_name='タイトル', max_length=40)
    year = models.IntegerField(verbose_name='学年', null=True)
    version = models.IntegerField(verbose_name='改訂版', default=1)
    is_visible = models.BooleanField(verbose_name='表示可否', default=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '教科書'

    def __str__(self):
        return self.title

#チャプター
class Diary(models.Model):
    """日記モデル"""

    title = models.CharField(verbose_name='タイトル', max_length=40)
    textbook = models.ForeignKey(TextBook, verbose_name='テキスト', on_delete=models.PROTECT, null=True)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'チャプター'

    def __str__(self):
        return self.title

class Question(models.Model):
    """質問"""

    chapter = models.ForeignKey(Diary ,verbose_name='チャプター', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    question_url = models.CharField(verbose_name='質問動画URL',  max_length=400)
    hint_photo = models.ImageField(verbose_name='ヒント写真', blank=True, null=True)

    answer_1 = models.TextField(verbose_name='回答1', blank=True, null=True)
    answer_2 = models.TextField(verbose_name='回答2', blank=True, null=True)
    answer_3 = models.TextField(verbose_name='回答3', blank=True, null=True)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '問題'

    def __str__(self):
        return self.title

class Answer(models.Model):
    """回答"""
    question = models.ForeignKey(Question, verbose_name="テスト", on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT, null=True)
    answer = models.CharField(verbose_name='タイトル', max_length=400)
    confidence = models.CharField(verbose_name='信頼度', default="-1", max_length=50)
    voice_file = models.FileField()
    auto_point = models.IntegerField(verbose_name="知識・技能", default=-1)
    auto_point2 = models.IntegerField(verbose_name="思考・判断・表現", default=-1)

    class Meta:
        verbose_name_plural = '回答'

    def __str__(self):
        return self.answer