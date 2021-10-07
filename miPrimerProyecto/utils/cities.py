import json

def get_all_cities()->list:
  filename = 'miPrimerProyecto/data/cities.json'
  file = open(filename, 'r')
  file_content = file.read()
  file.close()
  return json.loads(file_content)

def get_city_by_id(city_id: str)->dict:
  cities = get_all_cities()
  for city in cities:
    if (city['id'] == city_id):
      return city
