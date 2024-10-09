import requests 

baseurl = 'http://localhost:3000'   ## no / at the end

#
# api paths:
#
api_movies = '/movies'
api_top10 = '/movies/top10'
api_topNwithM = '/movies/topNwithM'
api_topNwithM_genre = '/movies/topNwithM/genre'

# genre = input("enter movie genre> ")

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

print()
print(body['message'])
print()
print(body['data'])

