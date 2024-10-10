import requests

baseurl = 'http://localhost:3000'  ## no / at the end

id = input('enter a movie id (e.g. 862)> ')

url = baseurl + "/movies/" + id

response = requests.get(url)

# print status_code
# if status_code == 200 then:
#   did we get a movie back, or is result empty dictionary { }?
#   if we got a movie back, output the Title and Revenue

  