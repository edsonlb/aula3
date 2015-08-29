import requests, sys

response = requests.get('http://apiedson.herokuapp.com/api/pessoa/?nome__icontains='+sys.argv[1],
                         auth=('admin', 'admin'))
data = response.json()

print data