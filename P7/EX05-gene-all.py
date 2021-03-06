import http.client
import json
import termcolor as tc
from Seq1 import Seq


def sequence_information(bases):  # created this function in order to return information about a sequence
    seq_info = Seq(bases)
    min_count = 0
    most_frecuent_base = ""

    tc.cprint("Total length:", 'green', end=' ')
    print(seq_info.len())

    for base, count in seq_info.count().items():
        # .items() returns the base and the count for each base
        percentage = round(count / seq_info.len() * 100, 2)  # round(,2) only shows to decimal numbers
        tc.cprint(f"{base}:", 'blue', end=' ')
        print(f" {count} ({percentage}%)")

        # here we are looking for the most frequent base
        if min_count < count:
            min_count = count
            most_frecuent_base = base

    # print the most frecuent base
    tc.cprint("Most frecuent Base:", 'green', end=' ')
    print(most_frecuent_base)


genes = dict(FRAT1='ENSG00000165879',  # defining the dictionary
             ADA='ENSG00000196839',
             FXN='ENSG00000165060',
             RNU6_269P='ENSG00000212379',
             MIR633='ENSG00000207552',
             TTTY4C='ENSG00000228296',
             RBMY2YP='ENSG00000227633',
             FGFR3='ENSG00000068078',
             KDR='ENSG00000128052',
             ANK2='ENSG00000145362')

for gene in genes:  # Go though every gene in list GENES

    server = 'rest.ensembl.org'  # Server address
    endpoint = '/sequence/id/' + genes[gene]
    options = '?content-type=application/json'  # We will get json information
    method = "GET"  #  GET method
    URL = server + endpoint + options

    #connecting with the server
    tc.cprint(f"\nConnecting to server: {server}", 'blue')
    tc.cprint(f"URL : {URL}", 'blue')

    connection = http.client.HTTPConnection(server)
    try:
        connection.request(method, endpoint + options)
    except ConnectionRefusedError:  # If the connection fail we print an error message
        print("ERROR! Cannot connect to the Server")
        exit()

    # response and status
    response = connection.getresponse()
    # .getresponse() method that returns the response information from the server

    tc.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

    data = response.read().decode("utf-8")  # It is necessary to decode the information
    # read JSON
    info_api = json.loads(data)  # loads(). is a method from JSON library (read JSON response)

    sequence = (info_api['seq'])
    description = info_api['desc']

    # RESULTS
    tc.cprint("Gene: ", 'green', end="")
    print(gene)

    tc.cprint("Description: ", 'green', end="")
    print(description)

    sequence_information(sequence)