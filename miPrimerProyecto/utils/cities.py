import json

def get_city_by_id(city_id: str)->dict:
  filename = 'miPrimerProyecto/data/cities.json'
  file = open(filename, 'r')
  file_content = file.read()
  file.close()
  cities = json.loads(file_content)
  for city in cities:
    if (city['id'] == city_id):
      return city
