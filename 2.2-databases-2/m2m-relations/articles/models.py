from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=25, default=None)


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    article_tag = models.ManyToManyField(Tag, related_name='article_tag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Csope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope_article')
    tag = models.ForeignKey(Tag, through='Article', through_field=('article_tag'), on_delete=models.CASCADE)
    base = models.BooleanField(default=False)
