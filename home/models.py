from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToCover
from project.phone import PhoneField
from solo.models import SingletonModel


class Seo(SingletonModel):

    title = models.TextField('Заголовок сайта')
    description = models.TextField('Описание сайта', null=True, blank=True)
    keywords = models.TextField('Ключевые слова', null=True, blank=True)

    def __str__(self):
        return 'Сео для сайта'

    class Meta:
        verbose_name = 'Сео для сайта'


class Metrics(SingletonModel):

    yandex = models.TextField('Яндекс метрика', null=True, blank=True)
    widget = models.TextField('Виджет', null=True, blank=True)

    def __str__(self):
        return 'Метрики для сайта'

    class Meta:
        verbose_name = 'Метрики и виджеты для сайта'


class InfoCompany(SingletonModel):

    name = models.CharField('Название компании', max_length=150)
    phone = PhoneField('Номер телефона')
    email = models.CharField('Почта', max_length=150)

    open_time = models.TimeField('Работаем с', null=True, blank=True)
    close_time = models.TimeField('Работаем по', null=True, blank=True)

    instagram = models.CharField('Ссылка на инстаграм', max_length=200, null=True, blank=True)
    youtube = models.CharField('ссылка на ютюб', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Основная информация компании"

    @property
    def get_format_phone(self):
        if self.phone:
            return f'{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:]}'
        return ''


class MainBlock(SingletonModel):

    caption = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Краткое описание')

    alt = models.CharField('Описание картинки - АЛЬТ', max_length=200)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='main_block/',
        format='JPEG',
        options={'quality': 85},
    )

    def __str__(self):
        return 'Блок основной'

    class Meta:
        verbose_name = 'Блок - Основной'


class AboutMeBlock(SingletonModel):

    caption = models.TextField('Заголовок')
    description = models.TextField('Краткое описание')

    frame_youtube = models.TextField('Код frame для видео с Youtube')

    def __str__(self):
        return 'Блок обо мне'

    class Meta:
        verbose_name = 'Блок - Обо мне'


class ProfitBlock(SingletonModel):

    caption = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Краткое описание')

    def __str__(self):
        return 'Блок выгода'

    class Meta:
        verbose_name = 'Блок - Выгода'


class Portfolio(models.Model):
    """Галерея Наши работы"""

    alt = models.TextField('Описание картинки - АЛЬТ')
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='portfolio/',
        format='JPEG',
        options={'quality': 85},
        processors=[
            ResizeToCover(width=800, height=800)
        ],
    )

    def __str__(self):
        return f'Работа id - {self.id}'

    class Meta:
        verbose_name = 'Блок - Наши работы'
        verbose_name_plural = 'Блок - Наши работы'


@receiver(pre_delete, sender=Portfolio)
def portfolio_delete(sender, instance, **kwargs):
    '''Удаляем картинки с диска при удалении записи'''
    if instance.image:
        instance.image.delete()


class BlockFlatRoof(SingletonModel):

    caption = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Краткое описание')
    about_info = models.TextField('О представленой информации', null=True, blank=True)

    def __str__(self):
        return 'Блок c ценами, плоская крыша'

    class Meta:
        verbose_name = 'Блок - Цены, плоская крыша'


class BlockSlopRoof(SingletonModel):

    caption = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Краткое описание')
    about_info = models.TextField('О представленой информации', null=True, blank=True)

    def __str__(self):
        return 'Блок c ценами, скатная крыша'

    class Meta:
        verbose_name = 'Блок - Цены, скатная крыша'


class WorkPriceImage(models.Model):

    work = models.CharField('Название работы', max_length=100)
    price = models.PositiveIntegerField('Цена')
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='price_images/',
        format='JPEG',
        options={'quality': 85},
        processors=[
            ResizeToCover(width=350, height=350)
        ],
    )

    block_float_roof = models.ForeignKey(
        BlockFlatRoof,
        verbose_name='Блок с ценой',
        on_delete=models.PROTECT,
        related_name='float_prices',
        null=True, blank=True
    )

    block_slop_roof = models.ForeignKey(
        BlockSlopRoof,
        verbose_name='Блок с ценой',
        on_delete=models.PROTECT,
        related_name='slop_prices',
        null=True, blank=True
    )

    def __str__(self):
        return self.work

    class Meta:
        verbose_name = 'Работа с ценой'
        verbose_name_plural = 'Работа с ценой'


@receiver(pre_delete, sender=WorkPriceImage)
def work_price_image_delete(sender, instance, **kwargs):
    '''Удаляем картинки с диска при удалении записи'''
    if instance.image:
        instance.image.delete()
