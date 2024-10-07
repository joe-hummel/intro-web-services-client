import requests

#################################################
# main
#
print('** client starting **')
print()

baseurl = 'http://localhost:3000/'

x = input('Enter integer x> ')

# 
# build the URL:
#
url = baseurl + 'incr/' + x

#
# call the service:
#
print()
print('url:', url)
print('Calling service...')

response = requests.get(url)

#
# display the result:
#
print()
print('status code:', response.status_code)
print('result:', response.text)

print()
print('** client done **')


