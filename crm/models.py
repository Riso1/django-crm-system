from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:service_detail', kwargs={'pk': self.pk})


class AdvertisingCampaign(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='campaigns',
        verbose_name='Рекламируемая услуга',
    )
    channel = models.CharField(max_length=150, verbose_name='Канал продвижения')
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Бюджет',
    )

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:campaign_detail', kwargs={'pk': self.pk})


class Lead(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Ф. И. О.')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    campaign = models.ForeignKey(
        AdvertisingCampaign,
        on_delete=models.CASCADE,
        related_name='leads',
        verbose_name='Рекламная кампания',
    )

    class Meta:
        verbose_name = 'Потенциальный клиент'
        verbose_name_plural = 'Потенциальные клиенты'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('crm:lead_detail', kwargs={'pk': self.pk})

    @property
    def is_active_customer(self):
        try:
            return self.customer is not None
        except Customer.DoesNotExist:
            return False


class Contract(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='contracts',
        verbose_name='Услуга',
    )
    document = models.FileField(
        upload_to='contracts/',
        blank=True,
        null=True,
        verbose_name='Документ',
    )
    signed_at = models.DateField(verbose_name='Дата заключения')
    valid_until = models.DateField(verbose_name='Действует до')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма',
    )

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:contract_detail', kwargs={'pk': self.pk})


class Customer(models.Model):
    lead = models.OneToOneField(
        Lead,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='Потенциальный клиент',
    )
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='Контракт',
    )

    class Meta:
        verbose_name = 'Активный клиент'
        verbose_name_plural = 'Активные клиенты'

    def __str__(self):
        return self.lead.full_name

    def get_absolute_url(self):
        return reverse('crm:customer_detail', kwargs={'pk': self.pk})