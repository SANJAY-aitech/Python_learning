'''String Manipulation'''

mobile = "8807963300"
masked = mobile[:2]+"******"+mobile[-2:]#indexing or slicing
print(masked)


anime_name = "OnE PuncH Man"
hero = "SaiTama"
formatted_str = f"{anime_name.title()} - {hero.title()}" #title()
print(formatted_str)

friend_name ="Genosis"
relation = "He is saitama friend"
replaced_name = relation.replace(relation[0],friend_name) #Replace
print(replaced_name)

message = "Your OTP is: 999000,please enter this"
otp = message.split(":")[1].split(",")[0].strip() #split(),strip()
print(otp)

coupon_code ="your code is Anime123 use this to get 90 off"
if "Anime123" in coupon_code:  #in 
    print("Offer Applied")

feedback = "The Anime was Good and fantastic"
position = feedback.find("Good") #find()
print(position)

name  = "sanjay thangarasu"
initial = "".join([word[0].upper() for word in name.split()]) #join(), upper(), split()
print(initial)

dirty_word = " hello    "
cleaned = dirty_word.strip()#strip()
print(cleaned)

word_count = len(feedback.split(" "))
print(word_count)