name = input("What is your name : ")
age = input("What is your age : ")
fav_movies = input("What is your favourate movies  :").split(",")
fav_songs = input("What is your favourate song : ")
User = {}
User["name"] =name
User["age"] =age
User["fav_movies"] =fav_movies
User["fav_song"] =fav_songs
for key,value in User.items():
    print(f"{key} : {value}")