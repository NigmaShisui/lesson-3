
wow = int(input("Number of your favorite fruites? "))
fruits = []


for x in range(wow):
    fr = input("Your Fav fruites?")
    fruits.append(fr)
    if x == "banana":   
        break
    elif x == "apple":
       print("Happy Eating")

print(fruits)
