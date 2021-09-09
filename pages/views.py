from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def about(request):
    my_name = "Hello, my name is Bob"
    return render(request, "about.html", {"my_name": my_name})

def list(request):
    import json
    import requests
    api_request = requests.get("https://api.openbrewerydb.org/breweries?per_page=50&by_city=san_antonio")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    return render(request, "list.html", {'api': api})

def search(request):
    import json
    import requests
    query = request.GET['q']
    api_request = requests.get("https://api.openbrewerydb.org/breweries?per_page=50&by_city=san_antonio&by_name=" + query)
    try:
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error... API call: " + api_request

    return render(request, "search.html", {'api': api, 'query': query})
