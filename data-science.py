users = {
    "id":0, "name": "Hero",
    "id":1, "name": "Dunn",
    "id":2, "name": "Sue",
    "id":3, "name": "Chi",
    "id":4, "name": "Thor",
    "id":5, "name": "Clive",
    "id":6, "name": "Hicks",
    "id":7, "name": "Devin",
    "id":8, "name": "Kate",
    "id":9, "name": "Ketlin"
}
friendships=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"]=[]

for i,j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number__of__friends(user):
    #"""Quantos amigos o usário tem?"""
    return len(user["friends"])

total_conections = sum(number__of__friends(user) for user in users)

from __future__ import division
num_users = len(users)
avg_conections = total_conections / num_users
num_friends_by_id = [(user["id"], number__of__friends(user)) for user in users]

sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)

def friends_of_friend_ids_bad(user):
    #"foaf" #friend of a friend
    return [foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]]

print([friend["id"] for friend in users[0]["friends"]])
print([friend["id"] for friend in users[1]["friends"]])
print([friend["id"] for friend in users[2]["friends"]])

#Olhe a linha 27 há 32
from typing import Counter
def not_the_same(user, other_user):
    #"Dois usuá não são os mesmos se possuem ids diferentes"
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    #"other_user não é um amigo se não está em user[“friends”]  isso é, se é not_the_same com todas as pessoas em"
    return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if not_the_same(user, foaf) and not_friends(user, foaf))

print(friends_of_friend_ids(user[3]))

interests = [
 

]