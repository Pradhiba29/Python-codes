sentence=input("Enter the sentence: ")
words=sentence.split()
for word in words:
    if len(word) > 4:
        print("valid word:",word)
        continue
    if word.lower()== "stop":
        break
    if word.isdigit():
        break
if(word==):
    print("stopped early because of the word stop")
else:
    print("processing finished normally")
