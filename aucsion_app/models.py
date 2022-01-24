from django.db import models
from django.contrib.auth.models import AbstractUser
from aucsion.utils.func import user_document, product_image


class User(AbstractUser):
    email = models.EmailField(
        'E-mail',
        unique=True,
        help_text='Required',
        error_messages={
            'unique': "A user with that E-mail already exists.",
        },
        db_index=True
    )
    document = models.ImageField(
        upload_to=user_document,
        verbose_name='Document',
        null=True,
        blank=True
    )
    first_name = models.TextField(
        'First name')
    last_name = models.TextField(
        'Last name')
    phone_number = models.CharField(
        'Full name', max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name', 'phone_number'
    ]

    @staticmethod
    def _create_user(password, email, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        user = User.objects.create(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, email, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, email, **extra_fields)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Seller(models.Model):
    user = models.ForeignKey(
        User, verbose_name='User - Seller', related_name='user_seller')
    expertise = models.CharField('expertise', max_length=44)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class SellerBlackList(models.Model):
    user = models.ForeignKey(
        User, verbose_name='User - Black List', related_name='user_blacklist')
    seller = models.ForeignKey(
        Seller, verbose_name='Seller - Black List', related_name='seller_blacklist')
    reason = models.TextField('Reason', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.seller}'

    class Meta:
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'


class Buyer(models.Model):
    user = models.ForeignKey(
        User, verbose_name='User - Buyer', related_name='user_buyer')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class BuyerBlackList(models.Model):
    buyer = models.ForeignKey(
        Buyer, verbose_name='User - Black List', related_name='buyer_blacklist')
    reason = models.TextField('Reason', null=True, blank=True)

    def __str__(self):
        return f'{self.buyer}'

    class Meta:
        verbose_name = 'Черный список покупателя'
        verbose_name_plural = 'Черный список покупателя'


class Aucsion(models.Model):
    start_datetime = models.DateTimeField(
        'Start datetime', null=True, blank=True, auto_now_add=True)
    end_datetime = models.DateTimeField(
        'End datetime', null=True, blank=True, auto_now_add=True)
    min_bet = models.IntegerField('Minimal bet', blank=True, null=True)
    max_bet = models.IntegerField('Max bet', blank=True, null=True)
    stock_price = models.IntegerField('Stock price')

    class Meta:
        verbose_name = 'Торг'
        verbose_name_plural = 'Торги'


class AucsionHistory(models.Model):
    buyer = models.ForeignKey(
        Buyer, verbose_name='Buyer - bet', related_name='buyer_bet')
    aucsion = models.ForeignKey(
        Aucsion, verbose_name='Aucsion - bet', related_name='aucsion_bet')
    bet = models.IntegerField('bet', blank=True, null=True)

    def __str__(self):
        return str(self.buyer) + ' - ' + str(self.aucsion)

    class Meta:
        verbose_name = 'История торга'
        verbose_name_plural = 'Истории торгов'


class Product(models.Model):
    document = models.ImageField(
        upload_to=product_image,
        verbose_name='product image',
    )
    seller = models.ForeignKey(
        Seller, verbose_name='Seller - Product', related_name='seller_product')
    aucsion = models.ForeignKey(
        Aucsion, verbose_name='Aucsion - product', related_name='aucsion_product')
    product_state = models.TextField('State')
    product_type = models.TextField('Type')

    price = models.IntegerField('Price')

    def __str__(self):
        return str(self.buyer) + ' - ' + str(self.aucsion)

    class Meta:
        verbose_name = 'История торга'
        verbose_name_plural = 'Истории торгов'


class Purchase(models.Model):
    datetime = models.DateTimeField(
        'datetime', null=True, blank=True, auto_now_add=True)
    final_price = models.IntegerField('Final price')
    buyer = models.ForeignKey(
        Buyer, verbose_name='Buyer - purchase', related_name='buyer_purchase')
    product = models.ForeignKey(
        Product, verbose_name='Purchase - product', related_name='product_purchase')

    def __str__(self):
        return str(self.buyer) + ' - ' + str(self.datetime)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class Delivery(models.Model):
    purchase = models.ForeignKey(
        Purchase, verbose_name='Delivery - purchase', related_name='delivery_purchase')
    address = models.TextField('address')
    delivery_type = models.TextField('Type')

    def __str__(self):
        return str(self.address) + ' - ' + str(self.delivery_type)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'


class Expert(models.Model):
    seller_report = models.TextField('Seller report')
    report = models.TextField('Report')

    class Meta:
        verbose_name = 'Эксперт'
        verbose_name_plural = 'Эксперты'


class Expertise(models.Model):
    expert = models.ForeignKey(
        Expert, verbose_name='Expert', related_name='expert_expertise')
    seller_report = models.TextField('Seller report')
    report = models.TextField('Report')
    product = models.ForeignKey(
        Product, verbose_name='Expretise - product', related_name='product_expretise')

    class Meta:
        verbose_name = 'Экспертиза'
        verbose_name_plural = 'Экспертизы'
