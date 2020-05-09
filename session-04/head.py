from pathlib import Path #to open a file

FILENAME = "RNU6_269P.txt"
file = Path(FILENAME)
data = file.read_text()
print(data) #printing all the data of the file

#Separete the data into lines
lines = data.split('\n')

print(f"First line of the {FILENAME} file is")
print(lines[0]) #printing the first line