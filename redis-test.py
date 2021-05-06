import redis
r = redis.Redis(host='localhost', port=6379, db=0)


while 1:
 inp = input("Method : ")
 if inp == "set":
   print("Enter the value")
   index = input("index : ")
   key = input ("key :")
   res = r.set(index, key)
   print(res)
 elif inp == "get":
   print("Enter the value")
   index = input("index : ")
   res = r.get(index)
   print(res.decode('utf8'))
   