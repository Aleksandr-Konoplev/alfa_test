from django.db import models
from slugify import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Category(models.Model):
    """ Модель категории. """
    name = models.CharField(max_length=255, verbose_name='Наименование категории', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True, blank=True)
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    """ Модель подкатегории. """
    name = models.CharField(max_length=255, verbose_name='Наименование подкатегории')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    image = models.ImageField(upload_to='subcategories/', verbose_name='Изображение')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='subcategories', verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """ Модель продукта. """
    name = models.CharField(max_length=255, verbose_name='Наименование продукта')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    image_200x200 = ImageSpecField(
        source='image',
        processors=[ResizeToFit(200, 200)],
        format='WEBP', options={'quality': 80}
    )
    image_600x600 = ImageSpecField(
        source='image',
        processors=[ResizeToFit(600, 600)],
        format='WEBP', options={'quality': 85}
    )
    image_1200x1200 = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200, 1200)],
        format='WEBP', options={'quality': 90}
    )

    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE,
        related_name='products', verbose_name='Подкатегория'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)