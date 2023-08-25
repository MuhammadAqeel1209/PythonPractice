import requests

# url = "https://www.ibm.com/"
# # url = "https://www.facebook.com/"

# req = requests.get(url)
# code = req.status_code
# head = req.request.headers 
# # Request headers contain more information about the resource to be fetched, or about the client requesting the resource. 
# print("Respons-->\t" ,req)
# print("\nStatus Code-->\t",code)
# print("\nHead of URL-->\t",head)
# print("\nData in Head of URL-->\t",req.headers['Date'])
# print("\nContent Type in Head of URL-->\t",req.headers['Content-Type'])
# print("\nEncoding in URL-->\t",req.encoding)
# print("\nText in URL-->\t",req.text[0:100])
# print("\nBody of Url-->\t",req.request.body)


# GET REQUEST  👇👇👇
# get_url = "http://httpbin.org/get"
# play_Load = {"name": "Joshep","ID": "123"}
# get = requests.get(get_url,params=play_Load)
# print("\nStatus Code-->\t",get.status_code)
# print("\nURL-->\t",get.url)
# print("\nBody of Url-->\t",get.request.body)
# print("\nContent Type in Head of URL-->\t",get.headers['Content-Type'])
# print("\nText in URL-->\t",get.text)
# print("\nJson in URL-->\t",get.json)
# print("\nArgs in Json in URL-->\t",get.json()['args'])



# POST REQUEST  👇👇👇
# post_url = "http://httpbin.org/post"
# play_Load = {"name": "Joshep","ID": "123"}
# post = requests.post(post_url,data=play_Load)

# print("\nStatus Code-->\t",post.status_code)
# print("\nURL-->\t",post.url)
# print("\nBody of Url-->\t",post.request.body)
# print("\nArgs in Json in URL-->\t",post.json()['form'])


# For example, some common headers in an HTTP request include:

# User-Agent: Information about the client making the request (usually a web browser or a bot).
# Host: The domain name of the server being contacted.
# Authorization: Credentials for authentication.
# Content-Type: The type of data being sent in the request body (for POST requests).
# Accept: The types of response content that the client can handle.
# And some common headers in an HTTP response include:

# Server: Information about the server software being used.
# Content-Type: The type of content in the response body.
# Content-Length: The size of the response body in bytes.
# Cache-Control: Instructions for caching the response.
# Location: Used in redirection responses.
