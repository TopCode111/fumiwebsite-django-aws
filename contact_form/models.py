# 箱の定義

from django.db import models


class Contact(models.Model):

    CHOICES_TOPICS = (("ご家族のお悩み", "ご家族のお悩み"), ("お金のお悩み", "お金のお悩み"),
                      ("お仕事のお悩み", "お仕事のお悩み"), ("日常生活のお悩み", "日常生活のお悩み"))

    name = models.CharField('お名前', max_length=20)
    email = models.EmailField('メールアドレス')
    phone = models.CharField('電話番号', max_length=20, blank=True, null=True)
    topics = models.CharField(
        'お問い合わせ内容', choices=CHOICES_TOPICS, max_length=300)
    message = models.TextField('詳細をお書きください')
