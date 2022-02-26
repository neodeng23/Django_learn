from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='')  # 字符串类型字段, max_length必须
    price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)  # 总精度7，小数点后2位
    pub = models.CharField("出版商", max_length=100, default='')
    market_price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'book'  # 改表名

    def __str__(self):
        return '%s %s %s' % (self.title, self.price, self.pub)
