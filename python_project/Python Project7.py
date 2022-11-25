#The task is to generate a random story every time user runs the program.
#Every time the user runs the program, we must produce a random tale. We'll first store the portions of the tales in distinct lists, and then use the Random module to choose random sections of the stories from those lists:
#To construct a random narrative, we first imported the random module, then built sections of the stories in separate lists, then randomly picked portions of the lists.


import random

print("Welcome to random story generator :")

n=int(input("Enter number of stories "))

print("Your",n,"random stories are :" )

part_1 = ['Long time ago', ' In the year 300 BC', 'Once upon a time']
part_2 = [' there lived a king.',' there lived a man named Harry.',
			' there lived a farmer.']
part_3 = [' One evening', ' One afternoon','One morning']
part_4 = [' he was passing by',' he was going for a picnic to ']
part_5 = [' the mountains', ' the garden', ' the park', ' the amusement park']
part_6 = [' he saw a man', ' he saw a young lady']
part_7 = [' who seemed to be in late 20s', ' who seemed very old and feeble']
part_8 = [' searching something.', ' digging a well on roadside.', ' playing with a young kid.']

i=1
while(i<=n):
    
    print(i,end=". ")
    print(random.choice(part_1)+random.choice(part_2)+
	random.choice(part_3)+random.choice(part_4) +
	random.choice(part_5)+random.choice(part_6)+
	random.choice(part_7)+random.choice(part_8))
    print()
    i+=1
    