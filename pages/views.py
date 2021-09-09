from django.shortcuts import render

def home(request):
  import json
  import requests

  api_request = requests.get("https://api.openbrewerydb.org/breweries?per_page=50&by_city=san_antonio")
  query = ""

  try:
      api = json.loads(api_request.content)
  except Exception as e:
      api = "Error..."

  return render(request, "home.html", {'api': api})

def about(request):
  my_name = "Hello, my name is Bob"
  return render(request, "about.html", {"my_name": my_name})
