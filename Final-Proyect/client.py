import http.client
import json
import termcolor

# Define the server and the server's port
PORT = 8080
SERVER = 'localhost'


termcolor.cprint("Test report.", 'red')
print("-------------------------------------- ")
print(" ")
print("TEST 1: ")
termcolor.cprint("Testing the main page.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
print(data1)

termcolor.cprint("Testing the rest of the endpoints.", 'red')
print(" ")
print(" ")
print("TEST 2:")
termcolor.cprint("Testing the listSpecies endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/listSpecies?limit=10")
print(" ")
print("Output:")
# This part of the client check if when json=1 is NOT selected, checking if the endpoint /listSpecies works properly

# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/listSpecies?limit=10")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
print(data1)

print(" ")
print(" ")
print("TEST 3")
termcolor.cprint("Testing the karyotype endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/karyotype?specie=human")
print(" ")
print("Output: ")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/karyotype?specie=human")

# Get the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

# This part of the client is going to  check the program when json=1 is NOT selected,
# checking if the endpoint /chromosomeLength works properly
print(" ")
print(" ")
print("TEST 4")
termcolor.cprint("Testing the chromosomeLength endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/chromosomeLength?specie=mouse&chromo=10")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/chromosomeLength?specie=mouse&chromo=10")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

# This part of the client check if when json=1 is NOT selected, checking if the endpoint /geneSeq works properly
print(" ")
print(" ")
print("TEST 5")
termcolor.cprint("Testing the geneSeq endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneSeq?gene=FRAT1")
print(" ")
print("Output:")
# Establishing connection to the Server

connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneSeq?gene=FRAT1")

# Getting the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

# This part of the client check if when json=1 is NOT selected, checking if the endpoint /geneInfo works properly
print(" ")
print(" ")
print("TEST 6")
termcolor.cprint("Testing the geneInfo endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneInfo?gene=FRAT1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneInfo?gene=FRAT1")

# Get the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

# This part of the client check if when json=1 is NOT selected, checking if the endpoint /geneCalc works properly
print(" ")
print(" ")
print("TEST 7")
termcolor.cprint("Testing the geneCalc endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneCalc?gene=FRAT1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneCalc?gene=FRAT1")

# Get the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

# This part of the client check if when json=1 is NOT selected, checking if the endpoint /geneList works properly
print(" ")
print(" ")
print("TEST 8")
termcolor.cprint("Testing the geneList endpoint when json format is not selected.", 'green')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneList?chromo=1&start=0&end=30000")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneList?chromo=1&start=0&end=30000")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()
print(data1)

###############################################################################

# This part of the client check if when json=1 is selected, the endpoint /listSpecies works properly
print(" ")
print(" ")
print("TEST 9")
termcolor.cprint("Testing the listSpecies endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/listSpecies?limit=10&json=1")
print(" ")
print("Output")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/listSpecies?limit=10&json=1")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /karyotype works properly
print(" ")
print(" ")
print("TEST 10")
termcolor.cprint("Testing the karyotype endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/karyotype?specie=human&json=1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/karyotype?specie=human&json=1")

# Getting the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /chromosomeLenght works properly
print(" ")
print(" ")
print("TEST 11")
termcolor.cprint("Testing the chromosomeLength endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/chromosomeLength?specie=mouse&chromo=10&json=1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/chromosomeLength?specie=mouse&chromo=10&json=1")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /geneSeq works properly
print(" ")
print(" ")
print("TEST 12")
termcolor.cprint("Testing the geneSeq endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneSeq?gene=FRAT1&json=1")
print(" ")
print("Output")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneSeq?gene=FRAT1&json=1")

# Getting the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /geneInfo works properly
print(" ")
print(" ")
print("TEST 13")
termcolor.cprint("Testing the geneInfo endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneInfo?gene=FRAT1&json=1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneInfo?gene=FRAT1&json=1")

# Get the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /geneCal works properly
print(" ")
print(" ")
print("TEST 14")
termcolor.cprint("Testing the geneInfo endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneCalc?gene=FRAT1&json=1")
print(" ")
print("Output:")
# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneCalc?gene=FRAT1&json=1")

# Get the response
response = connection.getresponse()

# Check The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)

# This part of the client check if when json=1 is selected, the endpoint /geneList works properly
print(" ")
print(" ")
print("TEST 15")
termcolor.cprint("Testing the geneList endpoint when json format is selected.", 'blue')
print(" ")
print("Input:")
print(" ")
print("http://127.0.0.1:8080/geneList?chromo=1&start=0&end=30000&json=1")
print(" ")
print("Output:")

# Establishing connection to the Server
connection = http.client.HTTPConnection(SERVER, PORT)
connection.request("GET", "/geneList?chromo=1&start=0&end=30000&json=1")

# Getting the response
response = connection.getresponse()

# Checking The status of the response
print('Response received: {}\n'.format(response.status, response.reason))

# Decoding the response
data1 = response.read().decode('utf-8')

# Closing the connection
connection.close()

# Creating a dictionary from the response received
dictionary_response = json.loads(data1)

# Print JSON text
print(dictionary_response)
