from pathlib import Path

FILENAME = "ADA.txt"

contents = Path(FILENAME).read_text()

#Remove the first line
lines = contents.split('\n')

#Build the body without the header and the \n characteres that is why we put "" empty instead of inserting inside \n.
body = "".join(lines[1:])

#Calculate the number of basis
print(f"The body of the sequence {FILENAME} is:{body}")
print(f"Length of the sequence: {len(body)}")