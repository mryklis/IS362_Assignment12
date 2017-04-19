import json
import requests

url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&offset=40&apikey=cca7ccbe60f842838bec1a4e5c7b8492'

response = requests.get(url)

data = json.loads(response.text)


for key in data:
    print key
