# requests is a library
import requests

r = requests.get("https://api.restful-api.dev/objects")
data = r.text
print(data)

r = requests.get("https://api.restful-api.dev/objects",headers={"test":"test"})
data = r.text
print(data)

request_data ={
    'title':'sudan-test'

}
r = requests.post("https://jsonplaceholder.typicode.com/posts",data=request_data)


'''
get to get data from server
Post to send data to server
put to update data on server
patch to update data on server
delete 

status Code
200
201
Unautorized acess
401
404
400
Server side error
500
503
POST = >
request payload or request  data dict 
'''



