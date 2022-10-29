import random, array

i = [8, 9, 10, 11, 12, 13, 14, 15, 16]
maxLen = random.choice(i)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowerAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '|', '/', '>', '<']

combined = numbers + lowerAlphabet + upperAlphabet + symbols

rand_num = random.choice(numbers)
rand_lower = random.choice(lowerAlphabet)
rand_upper = random.choice(upperAlphabet)
rand_sym = random.choice(symbols)

tmp = rand_num + rand_lower + rand_upper + rand_sym

for i in range(maxLen - 4):
    tmp += random.choice(combined)
    # convert tmp into an array and shuffle
    tmp_list = array.array('u', tmp)
    random.shuffle(tmp_list)

# traverse array
password = ""
for i in tmp_list:
    password += i

print(password)