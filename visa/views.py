from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import *


class VisaCategoryView(viewsets.ModelViewSet):
    queryset = VisaCategory.objects.all()
    serializer_class = VisaCategorySerializer


class CitizenCategoryView(viewsets.ModelViewSet):
    queryset = CitizenCategory.objects.all()
    serializer_class = CitizenCategorySerializer


class BuisnessCategoryView(viewsets.ModelViewSet):
    queryset = BuisnessCategory.objects.all()
    serializer_class = BuisnessCategorySerializer


class TravelView(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class UnnecessaryView(viewsets.ModelViewSet):
    queryset = Unnecessary.objects.all()
    serializer_class = UnnecessarySerializer


class HeaderSliderView(viewsets.ModelViewSet):
    queryset = HeaderSlider.objects.all()
    serializer_class = HeaderSliderSerializer


class DityoSliderView(viewsets.ModelViewSet):
    queryset = DityoSlider.objects.all()
    serializer_class = DityoSliderSerializer


class CountrySliderView(viewsets.ModelViewSet):
    queryset = CountrySlider.objects.all()
    serializer_class = CountrySliderSerializer


class CountriesView(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class ContinentView(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer


class FlagView(viewsets.ModelViewSet):
    serializer_class = FlagSerializer

    def get_queryset(self):
        queryset = Flag.objects.all()
        continent = self.request.query_params.get('continent')

        for flag in queryset:
            if not flag.name_uz and flag.country:
                flag.name_uz = Countries.objects.get(id = flag.country.id).name_uz
                flag.name_ru = Countries.objects.get(id = flag.country.id).name_ru
                flag.name_en = Countries.objects.get(id = flag.country.id).name_en
                flag.save() 

        if continent is not None:
            queryset = queryset.filter(continent__id = continent)
        return queryset