from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.


class GoodsType(models.Model):
    # 商品分类
    CATEGORY_TYPE = (
        ('1', "一级类目"),
        ('2', "二级类目"),
        ('3', "三级类目"),
    )
    name = models.CharField(
        default="",
        max_length=30,
        verbose_name="类别名",
        help_text="类别名")
    code = models.CharField(
        default="",
        max_length=30,
        verbose_name="类别code",
        help_text="类别code")
    desc = models.CharField(default="", verbose_name="类别描述", help_text="类别描述", max_length=50)
    category_type = models.CharField(
        max_length=30,
        choices=CATEGORY_TYPE,
        verbose_name="类目级别",
        help_text="类目级别")
    parent_type = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name="父类目级别",
        help_text="父目录", on_delete=models.CASCADE, related_name="sub_cat"
    )
    is_type = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(models.Model):
    # 品牌名称
    category = models.ForeignKey(
        GoodsType,
        related_name='brands',
        null=True,
        blank=True,
        verbose_name="商品类目", on_delete=models.CASCADE)
    name = models.CharField(
        default="",
        max_length=30,
        verbose_name="品牌名",
        help_text="品牌名", unique=True)
    desc = models.TextField(
        default="",
        max_length=200,
        verbose_name="品牌描述",
        help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '品牌名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    # 商品
    type = models.ForeignKey(
        GoodsType,
        verbose_name='商品名录',
        on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=30, default="", verbose_name="商品货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="卖出数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    good_nums = models.IntegerField(default=0, verbose_name="库存")
    market_price = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name='市场价')
    shop_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='售价')
    goods_brief = models.TextField(max_length=400, verbose_name="商品简短描述")
    goods_des = UEditorField(
        verbose_name=u"内容",
        imagePath="goods/images/",
        width=1000,
        height=300,
        filePath="goods/files/",
        default='')
    ship_free = models.BooleanField(verbose_name='是否免运费', default=True)
    goods_front_image = models.ImageField(
        upload_to="goods/images/",
        null=True,
        blank=True,
        verbose_name="封面图")
    is_new = models.BooleanField(verbose_name='是否是新品', default=False)
    is_hot = models.BooleanField(verbose_name='是否热卖', default=False)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_sn


class GoodsImage(models.Model):
    # 轮播小图
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="image",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='goods/images/', verbose_name="轮播图片")
    add_image = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Carousel(models.Model):
    # 轮播大图
    goods = models.ForeignKey(
        Goods,
        verbose_name="商品",
        related_name="images",
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(verbose_name='轮播编号')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播大图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class IndexAd(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品ID')

    category = models.ForeignKey(GoodsType, related_name='category', verbose_name="商品类目", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
