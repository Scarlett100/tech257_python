import requests, json

json_body = json.dumps({"postcodes" : ["PR3 0SG", "m45 6gn" "EX165BL"]}) # will allow us to add a pythin dict as a string so it will be vaild for the api

print(type(json_body))

headers = {"Content-Type": "application/json"} # change according to content type


post_multi_req = requests.post("https://api.postcodes.io/postcodes" , headers = headers , data =json_body) #  post requires header and body
headers = {"Content-Type": "application/json"}

print(post_multi_req.json())  # print

#
random_postcode = requests.get("https://api.postcodes.io/random/postcodes")
print(random_postcode.json())

#random_postcode = requests.get("https://api.postcodes.io/random/postcodes")
#print(random_postcode.json())


