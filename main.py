def checkword(text, searchedWord):
    words = text.split()
    if searchedWord in words:
        return True
    else:
        return False


try:
    file = open("text.txt", "r")
except FileNotFoundError:
    print ("Не знайдено файл text.txt.")
    input("Натисніть enter, щоб вийти...")
    exit()


while True:
    word = input("Введіть шукане слово: ")
    if len(word.split()) > 1:
        print("Ви ввели декілька слів. За умовою я можу шукати тільки одне слово.")
    elif word != "":
        break


file = open("text.txt", "r", encoding="utf-8")
lines = file.readlines()
paragraph = ""
print("\nСлово знайдено у наступних абзацах:\n")
i = 0
lastLine = lines[-1]
for line in lines:                      #Цикл перебирає кожен рядок, і,
    if line == "\n" or line == "":      #якщо рядок не є пустим, додає його до
        if checkword(paragraph, word):  #змінної paragraph. Коли цикл доходить до
           i = i + 1                    #пустого рядка, отримана змінна перевіряється
           print(paragraph)             #на збіг з шуканим словом.
        paragraph = ""                  #При збігі або при останньому рядку
                                        #paragraph виводиться на екран.
    elif line==lastLine:
        paragraph = paragraph + line
        if checkword(paragraph, word): 
           i = i + 1                   
           print(paragraph)             
        paragraph = ""
        
    else:
        paragraph = paragraph + line
if i == 0:
    print("Збігів немає.")
else:
    print("\nУсього збігів: ", i)
