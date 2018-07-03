from django.db import models


# Create your models here.
class ArtTag(models.Model):
    title = models.CharField(max_length=20, verbose_name='作品类别', unique=True, blank=False, db_index=True)

    # auto_now:每次修改的时间
    # auto_now_add:第一次添加的时间
    add_time = models.DateTimeField(verbose_name='添加的时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='修改的时间', auto_now=True)

