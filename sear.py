phrase = input("What Keyword are you searching for: ")
line_number = "Phrase not found"
a_file = open("filename.txt","r")
#filename.txt is where the full path of te text file you want to search through goes
for number, line in enumerate(a_file):
  if phrase in line:
    line_number = number
    break

a_file.close()

print(line_number)