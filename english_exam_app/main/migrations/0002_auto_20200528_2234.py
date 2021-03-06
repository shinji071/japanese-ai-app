# Generated by Django 2.2.2 on 2020-05-28 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('year', models.IntegerField(null=True, verbose_name='学年')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '教科書',
            },
        ),
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name_plural': 'チャプター'},
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('question_url', models.CharField(max_length=400, verbose_name='質問動画URL')),
                ('hint_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ヒント写真')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Diary', verbose_name='チャプター')),
            ],
            options={
                'verbose_name_plural': '問題',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=400, verbose_name='タイトル')),
                ('voice_file', models.FileField(upload_to='musics/')),
                ('auto_point', models.IntegerField(default=-1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Question', verbose_name='テスト')),
            ],
            options={
                'verbose_name_plural': '回答',
            },
        ),
        migrations.AddField(
            model_name='diary',
            name='text_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.TextBook', verbose_name='テキスト'),
        ),
    ]
