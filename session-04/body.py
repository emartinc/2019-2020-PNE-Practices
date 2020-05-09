from pathlib import Path

FILENAME = "U5"

contents = Path(FILENAME).read_text()

#Convert into lines and separates them
lines = contents.split('\n')

#Convert into text again to join the lines that have been separated previously
body = "\n".join(lines[1:])#this will return all the lines except the first one

#Print the body
print(f'The body of the {FILENAME} file is:')
print(body)