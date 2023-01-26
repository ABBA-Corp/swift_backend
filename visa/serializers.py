from rest_framework import serializers
from .models import *


class VisaCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VisaCategory
        fields = '__all__'


class CitizenCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CitizenCategory
        fields = '__all__'


class BuisnessCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BuisnessCategory
        fields = '__all__'


class TravelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Travel
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Images
        fields = '__all__'


class UnnecessarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Unnecessary
        fields = '__all__'


class HeaderSliderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HeaderSlider
        fields = '__all__'


class DityoSliderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DityoSlider
        fields = '__all__'


class CountrySliderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CountrySlider
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Countries
        fields = '__all__'

class ContinentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Continent
        fields = '__all__'

class FlagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flag
        fields = '__all__'