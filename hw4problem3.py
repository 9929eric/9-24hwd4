user_entry = input("Enter a word or sentence, please.")
print(user_entry)
n = len(user_entry) - 1
for i in range(len(user_entry)):
  print(user_entry[n],sep = '', end = '')
  n = n - 1
