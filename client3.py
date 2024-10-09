import requests
import jsons

class Movie:
  Movie_ID: int
  Title: str
  # and more

baseurl = 'http://localhost:3000'  ## no / at the end

#
# api paths:
#
api_movies = '/movies'

#
# get all the movies:
#
url = baseurl + api_movies

#
# call the web service:
#
response = requests.get(url)

#
# let's look at what we got back:
#
print()
print("status code:", response.status_code);

#
# deserialize and display:
#
body = response.json()  ## dictionary { message, data }

message = body['message']
movies = body['data']

print()
print("# of movies:", len(movies))
print()

i = 0
pagesize = 10
N = len(movies)

#
# show movies one page at a time:
#
while i < N:
  for r in range(i, min(i + pagesize, N)):
    row = movies[r]
    print(row["Movie_ID"], row["Title"], row["Revenue"])
    # m = jsons.load(movies[r], Movie)
    # print(m.Movie_ID, m.Title, m.Revenue)

  i += pagesize
  nextpage = input("Another page? [y/n] ")
  if nextpage != 'y':
    break
