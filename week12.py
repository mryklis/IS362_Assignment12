import json
import requests
from itertools import izip

url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&offset=40&apikey=cca7ccbe60f842838bec1a4e5c7b8492'

response = requests.get(url)

data = json.loads(response.text)

new_dict = {}
i = 0
for key, value in data['results'][i].items():
    new_dict
    i += 1

print new_dict


