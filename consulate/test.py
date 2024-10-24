import redis
import json
from redis.commands.json.path import Path
from connectToRedis import connection_redis

r = connection_redis()
# dict = {
#     'email': "form.emailAddress.data",
#     'password': "orm.password1.data", 
#     'firstName': "fa"
# }
# with open("newUser.json") as access_json:
#     data = json.load(access_json)
#     for key in data:
print(r.json().get("key *"))
tab = r.keys("*")
tab.sort()
print(tab)

# print(r.flushdb())