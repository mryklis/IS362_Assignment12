import json
import requests
import pandas as pd

url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&offset=40&apikey=cca7ccbe60f842838bec1a4e5c7b8492'

response = requests.get(url)

data = json.loads(response.text)

df = pd.DataFrame(data['results'])

print df

# df2 = []
#
# i = 0
# for values in df['multimedia']:
#
#     df2 = pd.DataFrame(values, index=[i])
#     df3 = pd.DataFrame().append(df2)
#     print df3
#     i += 1
#
# # df4 = pd.DataFrame(df3)
#
# print df3




