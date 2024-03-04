import requests




request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code) #the code of the homepage
print(request_bbc.content)  #content of the homepage
