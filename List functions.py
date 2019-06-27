lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "toby"]
friends.sort() # sort the list in acsending orders # like Alphavetical orders.

friends2 = friends.copy() # allows to copy from its value; friends2 is atrubutes to friends
#lucky_numbers.sort()
lucky_numbers.reverse() # sort the list in reverse in order.
#friends.pop() # removes the last of the element in the list
#friends.clear() # will clear everything inside the element in the list
#friends.remove("Jim") # anytime that you wanted to remove in the list
#friends.insert(1, "Kelly" ) # will take 2 parameters. first parameter will be index of where do you wanted to insert of the item; item that in pushed to the one and so others elemtments will be push up to the right
#friends.append("creed") # allows append another item ON TO THE END OF ITS LIST
#friends.extend(lucky_numbers) # will extend value from the its value
print(friends.index("Oscar")) # shows index of the element; ex Oscar is 3, Kevin is 0
print(friends.count("Jim")) # shows how many times in the value.
print(friends)
print(lucky_numbers)
print(friends2)
