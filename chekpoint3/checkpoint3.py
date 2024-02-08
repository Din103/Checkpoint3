#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
Name="Pedro"
Age=18
List=["Pedro","Juan","Maria"]
student=True
#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
Name_3letters=Name[0:3]
print(Name_3letters)
#Exercise 3: Use an index to grab the first element from your list.
first_element=List[0]
print(first_element)
#Exercise 4: Create a new number variable that adds 10 to your original number.
new_number=Age+10
print(new_number)
#Exercise 5: Use an index to get the last element in your list.
last_element=List[-1]
print(last_element)
#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list=names.split(",")
print(names_list)
#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase.Create a new string that takes the uppercase word and the rest of the original string.
first_word=names[0:5].upper()
new_string=first_word+names[5:]
print(new_string)
#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
sentence=f"My name is {Name} and I am {Age} years old"
print(sentence)
#Exercise 9: Print “hello world”.
