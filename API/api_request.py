import requests

post_codes_req =requests.get("https://api.postcodes.io/postcodes/se120nb") # https // makes it an endpoint
# print(post_codes_req)
# print(post_codes_req.status_code) # gives back just number
# print(post_codes_req.headers) #  getting back the headers
# print(post_codes_req.content) #
# print(type(post_codes_req.content)) # gives type (currently bytes)
# print(post_codes_req.json())
# print(type(post_codes_req.json())) # turns it into python dictionary

# How to access individual parts of the response
data_dict =post_codes_req.json()['result'] # just the values for specfic key
print(data_dict)
print(f"Region: {data_dict['country']}") # how to access specific values in dictionary.


