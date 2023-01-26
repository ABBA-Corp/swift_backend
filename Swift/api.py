from visa.views import *
from rest_framework import routers

router = routers.DefaultRouter()


router.register('visacategory', VisaCategoryView, basename='visacategory')
router.register('citizencategory', CitizenCategoryView, basename='citizencategory')
router.register('buisnesscategory', BuisnessCategoryView, basename='buisnesscategory')
router.register('travel', TravelView, basename='travel')
router.register('news', NewsView, basename='news')
router.register('images', ImagesView, basename='images')
router.register('unnecessary', UnnecessaryView, basename='unnecessary')
router.register('headerslider', HeaderSliderView, basename='headerslider')
router.register('dityoslider', DityoSliderView, basename='dityoslider')
router.register('countryslider', CountrySliderView, basename='countryslider')
router.register('countries', CountriesView, basename='countries')
router.register('continents', ContinentView, basename='continents')
router.register('flags', FlagView, basename='flags')