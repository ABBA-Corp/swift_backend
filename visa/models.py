from django.db import models


class VisaCategory(models.Model):
    country = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Visa Category'


class CitizenCategory(models.Model):
    country = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Citizen Category'
    

class BuisnessCategory(models.Model):
    country = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Buisness Category'
    

class Travel(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    flag = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Travel'


class News(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News'


class Images(models.Model):
    image = models.ImageField(null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Images'


class Unnecessary(models.Model):
    country = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name_plural = 'Unnecessary'


class HeaderSlider(models.Model):
    image = models.ImageField(null=True, blank=True)
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=10000, null=True, blank=True)
    location = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Header Slider'


class DityoSlider(models.Model):
    image = models.ImageField(null=True, blank=True)
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=10000, null=True, blank=True)
    location = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Dityo Slider'


class CountrySlider(models.Model):
    image = models.ImageField(null=True, blank=True)
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Country Slider'


class Countries(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    document_1_uz = models.TextField(max_length=2000, null=True, blank=True)
    document_1_ru = models.TextField(max_length=2000, null=True, blank=True)
    document_1_en = models.TextField(max_length=2000, null=True, blank=True)
    document_2_uz = models.TextField(max_length=2000, null=True, blank=True)
    document_2_ru = models.TextField(max_length=2000, null=True, blank=True)
    document_2_en = models.TextField(max_length=2000, null=True, blank=True)
    document_3_uz = models.TextField(max_length=2000, null=True, blank=True)
    document_3_ru = models.TextField(max_length=2000, null=True, blank=True)
    document_3_en = models.TextField(max_length=2000, null=True, blank=True)
    document_4_uz = models.TextField(max_length=2000, null=True, blank=True)
    document_4_ru = models.TextField(max_length=2000, null=True, blank=True)
    document_4_en = models.TextField(max_length=2000, null=True, blank=True)
    document_5_uz = models.TextField(max_length=2000, null=True, blank=True)
    document_5_ru = models.TextField(max_length=2000, null=True, blank=True)
    document_5_en = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'Countries'


class Continent(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'Continents'

class Flag(models.Model):
    image = models.ImageField(null=True, blank=True)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return '#{} {}'.format(self.id, self.name_en)

    class Meta:
        verbose_name_plural = 'Flags'