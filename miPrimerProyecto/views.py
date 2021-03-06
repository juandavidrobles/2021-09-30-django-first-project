from django.http import HttpResponse, JsonResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import datetime

from miPrimerProyecto.utils.cities import get_all_cities, get_city_by_id

def hello_world(request):
  return HttpResponse('Hello world from Django!')

def time(request):
  now = datetime.datetime.now()
  response = """
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Webpage from Django!!!</title>
</head>
<body>
  <p>La fecha y hora es: <strong>%s</strong></p>
</body>
</html>
  """ % now.strftime('%A %d-%m-%Y a las %I:%M %p')
  return HttpResponse(response)

def hello_json(request):
  return JsonResponse({'ok': True})

def get_image(request):
  image_url = 'https://images.unsplash.com/photo-1632922383279-62700518805c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1186&q=80'
  return HttpResponse('<img src="%s">' % image_url)

def load_image_by_id(request, city_id):
  city = get_city_by_id(city_id)
  if (city):
    return HttpResponse('<img src="%s">' % city['imageUrl'])

  return HttpResponse("""
  <h1>404 Page not found</h1>
  <strong>Vea también:</strong><br>
  <a href="/image/medellin">Ir a Medellin</a><br>
  <a href="/image/bogota">Ir a Bogota</a><br>
  <a href="/image/cali">Ir a Cali</a><br>
  <a href="/image/barranquilla">Ir a Barranquilla</a><br>
  """)

def load_image_by_id2(request, city_id):
  city = get_city_by_id(city_id)
  # template = loader.get_template('city.html')
  # render = template.render(city)
  # return HttpResponse(render)
  return render(request, 'city.html', city)

def load_city_list(request):
  cities = get_all_cities()
  render = loader.get_template('city-list.html').render({'cities': cities})
  return HttpResponse(render)

def test(request):
  template = loader.get_template('base-test.html')
  render = template.render({})
  return HttpResponse(render)
