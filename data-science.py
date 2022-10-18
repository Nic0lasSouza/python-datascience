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
from collections import defaultdict
from email.policy import default
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
    return all(not_the_same(friend, other_user)
    for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
    for friend in user["friends"]
    for foaf in friend["friends"]
    if not_the_same(user, foaf)
    and not_friends(user, foaf))

print(friends_of_friend_ids(user[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
def data_scientists_who_like(target_interest):
    return [user_id
    for user_id, user_interest in interests
    if user_interest == target_interest]

from collections import defaultdict
user_ids_interests = defaultdict(list)

for user_id, interest in interests:
    user_ids_interests[interest].append(user_id)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
    for interest in interests_by_user_id[user["id"]]
    for interested_user_id in user_ids_by_interest[interest]
    if interested_user_id != user["id"])
