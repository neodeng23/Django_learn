from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name="书名", max_length=50, default='')  # 字符串类型字段, max_length必须
    price = models.DecimalField(verbose_name="定价", max_digits=7, decimal_places=2, default=0.0)  # 总精度7，小数点后2位
    pub = models.CharField(verbose_name="出版商名称", max_length=100, default='')
    market_price = models.DecimalField(verbose_name="定价", max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField(verbose_name='是否活跃', default=True)

    class Meta:
        db_table = 'book'  # 该模型使用的数据表的名称

        verbose_name = '模型名(单数)'  # 给模型对象一个易于理解的名称(单数)，用于显示在/admin管理界面中

        verbose_name_plural = '模型名(复数)'  # 给模型对象复数形式的名称(复数)，用于显示在/admin管理界面中



    def __str__(self):
        return '%s | %s | %s | %s | %s' % (self.title, self.price, self.pub, self.market_price, self.is_active)
