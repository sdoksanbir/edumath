from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



# Branş Tablosu
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Branş Adı")  # Branş ismi
    description = models.TextField(null=True, blank=True, verbose_name="Branş Açıklaması")  # Branş açıklaması

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branş"
        verbose_name_plural = "Branşlar"


# Sınıf Tablosu
class Grade(models.Model):
    name = models.CharField(max_length=100, verbose_name="Sınıf Adı")  # Örnek: 5. Sınıf, 12. Sınıf
    category = models.CharField(max_length=100, verbose_name="Kategori")  # Sayısal, Eşit Ağırlık, vb.

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name = "Sınıf"
        verbose_name_plural = "Sınıflar"
        
        

class CustomUser(AbstractUser):
    # Kullanıcı Türü Seçenekleri
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Öğretmen'),
        ('student', 'Öğrenci'),
    ]

    # Kullanıcı türü alanı
    user_type = models.CharField(
        max_length=7,
        choices=USER_TYPE_CHOICES,  # Kullanıcı tiplerini USER_TYPE_CHOICES ile ilişkilendiriyoruz
        verbose_name='Kullanıcı Türü'
    )
    tc_no = models.CharField(
        max_length=11, 
        unique=True,
        verbose_name="TC Kimlik No"
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name="Telefon Numarası"
    )
    
    # Öğrenciler için
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sınıf")

    # Öğretmenler için
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Branş")

    # Ödeme durumu
    payment_status = models.BooleanField(default=False, verbose_name="Ödeme Durumu")
    payment = models.BooleanField(default=False, verbose_name="Ödeme Durumu")
    
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_user_type_display()})"

    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

