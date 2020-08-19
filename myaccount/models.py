from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

c_list = ['MANAGER', 'AI', 'CLOUD', 'BIGDATA', 'IOT']
CLASS_CHOICES = tuple(enumerate(c_list))

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, nickname, my_class, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            my_class=my_class,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    name = models.CharField(
        verbose_name='이름',
        max_length=10,
        blank=False
    )

    nickname = models.CharField(
        verbose_name='닉네임',
        max_length=10,
        blank=False,
        unique=True,
        default=''
    )

    my_class = models.SmallIntegerField(choices=CLASS_CHOICES, default=1, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return f"<{self.email} {self.name} {self.nickname}>"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_nickname(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin
