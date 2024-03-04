# Understanding APIs and HTTP

## 1. What are APIs? How are they used and why are they so popular?

Application Programming Interfaces also known as API'S can be defined as:

* Rules that allow different softwares to communicate.
    * eg. stock platform has stock information, trading app on phone communicates with the exchange through API's and gives you updates
    * API's are all about client and relationships.
    * eg. stock exchange = server trading 212 = client
    * app sends request, server responds
    * 4 different types of API's: **SOAP,RPC, Websocket and REST**
  
* API's are popular because they are the foundation of the digital world.
  * Api's are essentially middle men, they connect the server to client, they link the experience to you. 



## 2. What is a REST API? What makes an API RESTful? What are the REST guidelines?

 Representational State Transfer can be shortened to rest.

A RESTful API is like a bridge that allows two computers to talk to each other safely on the internet, providing a structured way for them to share data and commands, communication  secure.


## 3. What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

 * HTTP: The Hypertext Transfer Protocol 
 * Essentially request and response
 * If you enter a request with info (eg. a url) it should respond with the page
 * Transports! takes info between server and client. eg

## 6. What are the 5 HTTP verbs and what do they do?

GET, PUT, DELETE, PATCH and Post are functions that clients use to access server data. 

**GET**: requests and retrieves data from a server. eg. writing in a url and it appearing after hitting enter.

**POST**: Submits new data to URL on server. eg. posting a review or uploading a file

**PUT**: Updates a resource or creates a new resource if it doesn't exist. 

**PATCH**: partial update. eg. changing name of client on an account from Gregg to Asa.

**DELETE**:  delete the resource (DB, URL)

## 7. What is statelessness? Show examples of “stateless” and “stateful” http requests.

A stateless API doesn't utilise the server to maintain a client session, every request is separate and independent of others, no info is stored after collection.
  * Imagine you have an allergy and every time you want to add onto your order you must say, "Hey, i'm allergic to xyz"
  * With a stateful API there is some memory of this and it is known you have your allergy and do not need to mention it each time you order more food, because the kitchen remembers.

Essentially: a stateful API has a record of previous requests information unlike a stateless API does not. 


## 8. What is caching?

Cache is essentially a non permanent storage layer. It essentially allows requests to be retrieved quicker because the request has been stored before, within the cache.
It is normally stored within the RAM. You may sometimes find that need to clear your cache to get things to work.
