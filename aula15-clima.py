import requests
import json
import datetime

cidade = input('Escreva aqui a cidade desejada: ')
print ('')
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade +'&appid=2f1a37a09e6db07650e458f6b8304dcd')

clima = json.loads(requisicao.text)
print ('####', cidade +':', '####', '\t', datetime.datetime.now())
print ('Condição do tempo: ', clima['weather'][0]['main'])
print ('Descrição: ', clima['weather'][0]['description'])
print ('Temperatura atual: ', float(clima['main']['temp'] - 273.15))
print ('Sensação térmica: ', float(clima['main']['feels_like'] - 273.15))
print ('Temperatura mínima: ', float(clima['main']['temp_min'] - 273.15))
print ('Temperatura máxima: ', float(clima['main']['temp_max'] - 273.15))





