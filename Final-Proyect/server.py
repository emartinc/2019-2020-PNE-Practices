import socketserver
import http.server
import http.client
import json
from Seq import Seq

HOSTNAME = "rest.ensembl.org"
METHOD = "GET"
PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def convert_dict(self, path): # function in order to build a dictionary
        Dictionary = dict()

        if '?' in path: # if the ? is in my path it means that my path has at least one variable
            key_value = path.split('?')[1]
            key_value = key_value.split(' ')[0]
            list1 = key_value.split('&')

            for key_and_value in list1:
                name_parameter = key_and_value.split('=')[0]
                value_parameter = key_and_value.split('=')[1]
                Dictionary[name_parameter] = value_parameter

        return Dictionary

    def do_GET(self):
        HTTP_CODE = 200


# creating an if... elif... else... statement in order to make decisions depending on the selected endpoint

        if self.path == '/': # when the only additional thing that appears on the url is a / we print the main page, the index page
            jsonvalue = 0 # when the json parameter is not present the server will send a response with the html pages instead
            contents = 'index.html' # the html page

            with open(contents, 'r') as a:
                contents = a.read()
                a.close()

        elif '/listSpecies' in self.path: # here we start adding things, if in the url appears /listspecies (first endpoint)
            if 'limit' in self.path: #if the parameter limit is specified that number is the amount of species that are going to be shown
                try:
                    arguments = self.convert_dict(self.path) #using the function defined previously in order to create a dictionary with all the species
                    limit = arguments['limit'] #the limit parameter indicates the maximum number of species to show
                    # making the petition to the REST API
                    ENDPOINT = "/info/species?content-type=application/json"
                    headers = {'User-Agent': 'http-client'}
                    connection = http.client.HTTPConnection(HOSTNAME) #stablishing the connection with the client
                    connection.request(METHOD, ENDPOINT, None, headers)
                    response = connection.getresponse() #this is in order to get the response
                    text_json = response.read().decode("utf-8")
                    connection.close() # closing/stopping the connection with the server

                    data1 = json.loads(text_json)
                    species = data1['species']

                except TypeError: # we do this in order to make sure that if any error is done when entering the data it appears
                    HTTP_CODE = 404
                    # making the petition to the REST API
                    ENDPOINT = "/info/species?content-type=application/json"
                    headers = {'User-Agent': 'http-client'}
                    connection = http.client.HTTPConnection(HOSTNAME)
                    connection.request(METHOD, ENDPOINT, None, headers)
                    r1 = connection.getresponse()
                    text_json = r1.read().decode("utf-8")
                    connection.close()
                    data1 = json.loads(text_json)
                    species = data1['species']
                    limit = len(species)

                try:
                    int(limit)

                except ValueError: # we do this in order to make sure that if any error is done when entering the data it appears
                    HTTP_CODE = 404
                    limit = len(species)

            else:
                # making the petition to the REST API
                ENDPOINT = "/info/species?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                text_json = r1.read().decode("utf-8")
                connection.close()
                data1 = json.loads(text_json)
                species = data1['species']
                limit = len(species)

            count = 0 # setting the counter
            List = []

            for one in species:
                specie = one['name']
                List.append(specie)
                count = count + 1 #each time one new specie is added to the list the counter sums one

                if int(count) == int(limit): #when the number of species is reached we stop
                    break

            Dictionary = {}
            Dictionary['Species'] = List

            if 'json=1' in self.path: # to show the info of the page in json format
                jsonvalue = 1
                contents = json.dumps(Dictionary)

            else:
                jsonvalue = 0 #to show the info of the page as an html intead of a json
                # the defined html page is very short and simple, thats why is inserted inside the code. this html page contains the list of the species
                contents = """  
                            <html>

                  <body style="background-color: lightgreen;">

                    <h1>List of all species</h1>

                            <ul>"""

                count = 0

                for one in species:
                    contents = contents + '<li>' + one['name'] + '</li>'
                    count = count + 1

                    if int(count) == int(limit):
                        break

                # modifying the previous html page depending on the species
                contents = contents + """

                            </ul>

                            </body>

                            </html>

                            """

        elif '/karyotype' in self.path: # endpoint to return information about the karyotype of a specie
            arguments = self.convert_dict(self.path) # using the previously created function in order to create a dictionary with the values

            try:
                name = arguments['specie']
                # making the petition to the REST API
                ENDPOINT = "/info/assembly/" + name + "?"
                headers = {'Content-Type': 'application/json'}
                connection = http.client.HTTPConnection(HOSTNAME) #stablishing the connection
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                text_json = r1.read().decode("utf-8")
                connection.close()
                response = json.loads(text_json)
                karyotype = response['karyotype']
                Dict = {}
                Dict['karyotype'] = response['karyotype']

                if 'json=1' in self.path: # printing the result in a json format
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0 # showing the info as an html page
                    # the defined html page is very short and simple, thats why is inserted inside the code. this html page contains the info about the karyotype
                    contents = """

                                <html>

                      <body style="background-color: lightblue;">

                        <h1>Karyotype</h1>

                                <ul>"""

                    for one in karyotype:
                        contents = contents + '<li>' + one + '</li>'

                    contents = contents + """

                                </ul>

                                </body>

                                </html>

                                """

            except KeyError: # taking care of the error that appears when an invalid name is inserted
                jsonvalue = 0
                HTTP_CODE = 404
                # the html page that appears throws a warning message
                contents = """
                            <html>

                  <body style="background-color: red;">

                    <h1>Invalid name enterd, please type a correct one</h1>

                            </body>

                            </html>

                            """

        elif '/chromosomeLength' in self.path: # endpoint to return the length of the chromosome of a given specie
            arguments = self.convert_dict(self.path) # using the previously created function in order to create a dictionary with the values

            try:
                Dict = {}
                Dict['name_specie'] = arguments['specie']
                Dict['name_chromo'] = arguments['chromo']
                name_specie = arguments['specie'] #parameter
                name_chromosome = arguments['chromo'] #parameter
                # making the petition to the REST API
                ENDPOINT = "/info/assembly/" + name_specie + "?"
                headers = {'Content-Type': 'application/json'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                print('Response received: {}\n'.format(r1.status, r1.reason))
                data1 = r1.read().decode('utf-8')
                connection.close()
                response = json.loads(data1) #transform into data structures

                if 'json=1' in self.path:  # printing the data in json format
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0  #printing the data in html format
                    response = response['top_level_region']
                    # the defined html page is very short and simple, thats why is inserted inside the code. this html page contains the info about the length of the chromosome
                    contents = """
                                  <html>

                    <body style="background-color: pink;">

                    <h1>Length of the Chromosome</h1>

                                    """

                    ok = False

                    for element in response:  # if the entered name of a chromosome is valid calculate the length of that chromosome
                        if element['name'] == name_chromosome:
                            contents = contents + str(element['length'])
                            ok = True

                    if not ok:
                        contents = contents + str(0)

                    contents = contents + """

                                </body>

                                </html>

                                """

            except KeyError: # # taking care of the error that appears when an invalid name is inserted
                jsonvalue = 0
                HTTP_CODE = 404
                # the html page that appears throws a warning message
                contents = """

                    <html>

                    <body style="background-color: red;">

                    <h1>Invalid name entered, please type a correct one</h1>

                        </body>

                        </html>

                        """

        elif "/geneSeq" in self.path: # endpoint to return the sequence of a given human gene
            arguments = self.convert_dict(self.path) # using the previously created function in order to create a dictionary with the values
            try:
                gene_name = arguments['gene'] #paramenter (the data is stored in a dictionary)
                # making the petition to the REST API
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                data1 = r1.read().decode('utf-8')
                connection.close()

                response = json.loads(data1) # transform the into data structure
                id = response['data'][0]['id']

                connection.request('GET', '/sequence/id/' + id + '?content-type=application/json')
                r1 = connection.getresponse()
                data1 = r1.read().decode('utf-8')
                connection.close()

                response = json.loads(data1)
                DNAsequence = response['seq']

                Dict = {}
                Dict['DNAsequence'] = response['seq']

                if 'json=1' in self.path: # printing the data in json format
                    jsonvalue = 1
                    contents = json.dumps(Dict) #

                else:
                    jsonvalue = 0 #printing the data in html format
                    # the defined html page is very short and simple, thats why is inserted inside the code. this html page contains sequence of a given human gene
                    contents = """

                                  <html>

                        <body style="background-color: lightgreen;">

                          <h1>DNA sequence</h1>

                            """ + DNAsequence + """

                                  </body>

                                  </html>

                                  """

            except KeyError:  # taking care of the error that appears when an invalid name is inserted
                jsonvalue = 0
                HTTP_CODE = 404
                # the html page that appears throws a warning message
                contents = """

                        <html>

                        <body style="background-color: red;">

                        <h1>Invalid name entered, please type a correct one</h1>

                            </body>

                            </html>

                            """

        elif "/geneInfo" in self.path: # endpoint thata when entered returns all the info about a human gene(length, start, end nid, chromosome...)
            arguments = self.convert_dict(self.path) # using the previously created function in order to create a dictionary with the values
            try:
                gene_name = arguments['gene']
                # making the petition to the REST API, stablising the connection with it.
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                data1 = r1.read().decode('utf-8')
                connection.close()
                response = json.loads(data1) #transform into data structure
                idd = response['data'][0]['id']

                ENDPOINT = "/overlap/id/" + idd + "?feature=gene;content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                data1 = r1.read().decode('utf-8')
                connection.close()
                response1 = json.loads(data1) #transform into data structure
                # working with the data in order to obtain all the needed info
                start = response1[0]['start']
                end = response1[0]['end']
                length = end - start
                chromosome = response1[0]['assembly_name']
                # storing all the data in dictionaries
                Features = {}
                Features['start'] = response1[0]['start']
                Features['end'] = response1[0]['end']
                Features['length'] = length
                Features['chromo'] = response1[0]['assembly_name']
                Features['id'] = idd

                if 'json=1' in self.path: # transforming the data into json format and returning that
                    jsonvalue = 1
                    contents = json.dumps(Features) # this helps us in order to work with the stored data

                else:
                    jsonvalue = 0 # returning the data in html format
                    # the html page is very simple, thats why its included directly in the code
                    contents = """

                                      <html>

                            <body style="background-color: lightgreen;">

                              <h1>Information about the Gene</h1>

                                """ + 'Start:' + str(start) + '\nEnd:' + str(end) + '\nLength:' + str(

                        length) + '\nChromosome:' + chromosome + '\nId:' + idd + """

                                      </body>

                                      </html>

                                      """

            except KeyError: # error that is raised whenever an invalid name is inserted
                jsonvalue = 0
                HTTP_CODE = 404
                # printed in html format
                contents = """

                        <html>

                        <body style="background-color: red;">

                        <h1>Invalid name, please enter a correct one</h1>

                            </body>

                            </html>

                            """

        elif '/geneCalc' in self.path: # endpoint that
            arguments = self.convert_dict(self.path) # using the previously created function in order to create a dictionary with the values

            try:
                gene_name = arguments['gene']
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                data1 = r1.read().decode('utf-8')
                connection.close()


                response = json.loads(data1) # transform into data structures
                idd = response['data'][0]['id']

                ENDPOINT = "/sequence/id/" + idd + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                r1 = connection.getresponse()
                print('Response received: {}\n'.format(r1.status, r1.reason))

                data1 = r1.read().decode('utf-8')
                response = json.loads(data1) #transform into data structures
                DNAsequence = response['seq']
                seq = Seq(DNAsequence)
                length = len(DNAsequence)

                #doing the calculations of the percentage of each base using the function in the class Seq
                percentage_A = seq.perc('A')
                percentage_C = seq.perc('C')
                percentage_T = seq.perc('T')
                percentage_G = seq.perc('G')

                Calculations = {} #creating a dictionary to store all the calculations performed previously
                Calculations['length'] = length
                Calculations['Perc_A'] = percentage_A
                Calculations['Perc_c'] = percentage_C
                Calculations['Perc_T'] = percentage_T
                Calculations['Perc_G'] = percentage_G

                if 'json=1' in self.path: # return the data in json format
                    jsonvalue = 1
                    contents = json.dumps(Calculations)

                else:
                    jsonvalue = 0 #return the data in html format
                    #html file that is very simple and theres no need to create a separate html file
                    contents = """

                                      <html>

                            <body style="background-color: lightgreen;">

                              <h1>Total Lenght and Percentage of each Base</h1>

                                """ + 'Lenght' + str(length) + '<br>' + "Percentage of A's" + str(
                        percentage_A) + '<br>' + "Percentage of C's" + str(percentage_C) + '<br>' + "Percentage of T's" + str(
                        percentage_T) + '<br>' + "Percentage of G's: " + str(percentage_G) + \
                               """

                                      </body>

                                      </html>

                                      """

            except KeyError: # error that is shown whenever the input is wrong
                jsonvalue = 0
                HTTP_CODE = 404
                #error html file
                contents = """

                        <html>

                        <body style="background-color: red;">

                        <h1>Invalid Name, please enter a correct one</h1>

                            </body>

                            </html>

                            """

        elif "/geneList" in self.path: # endpoint that returns the names of the genes located in the chromosome chromo from the start to end positions
            arguments = self.convert_dict(self.path) # # using the previously created function in order to create a dictionary with the values

            try:
                chromo = arguments['chromo']  #parameter
                start = arguments['start'] # parameter
                end = arguments['end'] #parameter


                #stablishing the connection with the srever
                ENDPOINT = "/overlap/region/human/" + str(chromo) + ":" + str(start) + "-" + str(end) + "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"
                headers = {'User-Agent': 'http-client'}
                connection = http.client.HTTPConnection(HOSTNAME)
                connection.request(METHOD, ENDPOINT, None, headers)
                response = connection.getresponse()
                data = response.read().decode("utf-8")
                connection.close()

                response2 = json.loads(data) # transform into data structures
                stop = int(end) - int(start)
                count = 0 # setting a counter
                List = []

                for possiblegene in response2:
                    if 'feature_type' in possiblegene and possiblegene['feature_type'] == 'gene':
                        List.append(possiblegene['external_name'])
                        count = count + 1

                        if count == stop:
                            break

                Dict = {} # generating a dictionary thata is going to contain all the genes
                Dict['Gene'] = List

                if 'json=1' in self.path: # printing tha data in json format
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0 # printing tha data in html format
                    # creating an html file, it is very simple, that is why is inserted inside the code
                    contents = """

                                                    <html>

                                          <body style="background-color: lightgreen;">

                                            <h1>Name of Each Gene</h1>

                                                    <ul>"""

                    count = 0

                    for possiblegene in response2:
                        if 'feature_type' in possiblegene and possiblegene['feature_type'] == 'gene':
                            contents = contents + '<li>' + possiblegene['external_name'] + '</li>'
                            count = count + 1

                            if count == stop:
                                break

                    contents = contents + """

                                                    </ul>

                                                    </body>

                                                    </html>

                                                    """

            except KeyError: # this is shown each time the input is wrong
                jsonvalue = 0 # the response is in html format
                HTTP_CODE = 404
                 # ceating an error file
                contents = """

                                        <html>

                                        <body style="background-color: red;">

                                        <h1>Invalid Name, please enter a correct one</h1>

                                            </body>

                                            </html>

                                            """

        else: # if the first endpoint is different from the ones established an error html file appears
            jsonvalue = 0
            HTTP_CODE = 404
            contents = 'error.html'

            with open(contents, 'r') as a:
                contents = a.read()
                a.close()

        self.send_response(HTTP_CODE)

        # Creating a loop to choose what 'content type' in headers should be added
        if jsonvalue == 1:
            self.send_header('Content-Type', 'application/json')

        else:
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


# Main Program
# -- Set the new handler

Handler = TestHandler

socketserver.TCPServer.allow_reuse_address = True

# -- Open the socket server

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

