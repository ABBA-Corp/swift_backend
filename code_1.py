import json 
from translate import Translator  
import requests
# from visa.models import Countries

def translate(from_lang, to_lang, text):
	url = "https://microsoft-translator-text.p.rapidapi.com/translate"

	querystring = {"to[0]":to_lang,"api-version":"3.0","from":from_lang,"profanityAction":"NoAction","textType":"plain"}

	payload = [{"Text": text}]
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "c96d80c507msh88bbe2009f24da3p136a45jsn51827ea67f47",
		"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
	}

	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

	return json.loads(response.text)[0]['translations'][0]['text']

translator_ru = Translator(to_lang = 'ru')
translator_uz = Translator(to_lang = 'uz')

file = open('all.json')
countries = json.load(file)
file.close()

for country in countries:
	country_en = country['name']['common']
	# country_ru = translate('en', 'ru', country_en)
	# country_uz = translate('en', 'uz', country_en)
	# Countries.objects.create(name_en = country_en, name_ru = country_ru, name_uz = country_uz)
	print(country_en)