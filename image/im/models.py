from django.db import models

# Create your models here.

class ImageModel(models.Model):
    """图片模型"""
    json_result = models.CharField(verbose_name="序列化之后的结果", max_length=255)
    image = models.ImageField(upload_to='img', verbose_name='图片')

    class Meta:
        db_table = "im"
        verbose_name = "图片识别"
        verbose_name_plural = verbose_name
