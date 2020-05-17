import socketserver
import termcolor
import http.server
import http.client
import json
from Seq import Seq

HOSTNAME = "rest.ensembl.org"
METHOD = "GET"
PORT = 8000

class TestHandler(http.server.BaseHTTPRequestHandler):
    def convert_dict(self, path):
        Dict = dict()

        if '?' in path:
            keyvalue = path.split('?')[1]
            keyvalue = keyvalue.split(' ')[0]
            listt = keyvalue.split('&')

            for keyandvalue in listt:
                name_parameter = keyandvalue.split('=')[0]
                value_parameter = keyandvalue.split('=')[1]
                Dict[name_parameter] = value_parameter

        return Dict

    def do_GET(self):
        HTTP_CODE=200

        if self.path == '/':
            jsonvalue = 0
            contents = 'index.html'

            with open(contents, 'r') as a:
                contents = a.read()
                a.close()

        elif '/listSpecies' in self.path:

            if 'limit' in self.path:
                try:
                    keyandvalue = self.convert_dict(self.path)
                    limit = keyandvalue['limit']
                    ENDPOINT = "/info/species?content-type=application/json"
                    headers = {'User-Agent': 'http-client'}
                    conn = http.client.HTTPConnection(HOSTNAME)
                    conn.request(METHOD, ENDPOINT, None, headers)
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")

                    conn.close()
                    data1 = json.loads(text_json)
                    species = data1['species']

                except TypeError:
                    HTTP_CODE = 404
                    ENDPOINT = "/info/species?content-type=application/json"
                    headers = {'User-Agent': 'http-client'}
                    conn = http.client.HTTPConnection(HOSTNAME)
                    conn.request(METHOD, ENDPOINT, None, headers)
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")

                    conn.close()
                    data1 = json.loads(text_json)
                    species = data1['species']
                    limit = len(species)

                try:
                    int(limit)

                except ValueError:
                    HTTP_CODE = 404
                    limit = len(species)

            else:
                ENDPOINT = "/info/species?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                conn.close()

                data1 = json.loads(text_json)
                species = data1['species']
                limit = len(species)

            count = 0
            List = []

            for one in species:
                specie = one['name']
                List.append(specie)
                count = count + 1

                if int(count) == int(limit):
                    break

            Dict = {}
            Dict['Species'] = List

            if 'json=1' in self.path:
                jsonvalue = 1
                contents = json.dumps(Dict)

            else:
                jsonvalue = 0
                contents = """
                            <html>

                  <body style="background-color: green;">

                    <h1>List of all species</h1>

                            <ul>"""

                count = 0

                for one in species:
                    contents = contents + '<li>' + one['name'] + '</li>'
                    count = count + 1

                    if int(count) == int(limit):
                        break

                contents = contents + """

                            </ul>

                            </body>

                            </html>

                            """

        elif '/karyotype' in self.path:
            keyandvalue = self.convert_dict(self.path)

            try:
                name = keyandvalue['specie']
                ENDPOINT = "/info/assembly/" + name + "?"
                headers = {'Content-Type': 'application/json'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                conn.close()

                response = json.loads(text_json)
                karyotype = response['karyotype']
                Dict = {}
                Dict['karyotype'] = response['karyotype']

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0
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

            except KeyError:
                jsonvalue = 0
                HTTP_CODE = 404
                contents = """
                            <html>

                  <body style="background-color: lightblue;">

                    <h1>Invalid Name</h1>

                            </body>

                            </html>

                            """

        elif '/chromosomeLength' in self.path:
            keyandvalue = self.convert_dict(self.path)

            try:
                Dict = {}
                Dict['name_specie'] = keyandvalue['specie']
                Dict['name_chromo'] = keyandvalue['chromo']
                name_specie = keyandvalue['specie']
                name_chromo = keyandvalue['chromo']
                ENDPOINT = "/info/assembly/" + name_specie + "?"
                headers = {'Content-Type': 'application/json'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                print('Response received: {}\n'.format(r1.status, r1.reason))
                data1 = r1.read().decode('utf-8')
                conn.close()

                response = json.loads(data1)

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0
                    response = response['top_level_region']
                    contents = """
                                  <html>

                    <body style="background-color: pink;">

                    <h1>Length of the Chromosome</h1>

                                    """

                    ok=False

                    for number in response:
                        if number['name'] == name_chromo:
                            contents = contents + str(number['length'])
                            ok=True

                    if not ok:
                        contents = contents + str(0)

                    contents = contents + """

                                </body>

                                </html>

                                """

            except KeyError:
                jsonvalue = 0
                HTTP_CODE=404
                contents = """

                    <html>

                    <body style="background-color: lightblue;">

                    <h1>Invalid Name</h1>

                        </body>

                        </html>

                        """

        elif "/geneSeq" in self.path:
            keyandvalue = self.convert_dict(self.path)
            try:
                gene_name = keyandvalue['gene']
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                data1 = r1.read().decode('utf-8')
                conn.close()
                response = json.loads(data1)
                id = response['data'][0]['id']
                conn.request('GET', '/sequence/id/' + id + '?content-type=application/json')
                r1 = conn.getresponse()
                data1 = r1.read().decode('utf-8')
                conn.close()

                response = json.loads(data1)
                DNAsequence = response['seq']
                Dict = {}
                Dict['DNAsequence'] = response['seq']

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0
                    contents = """

                                  <html>

                        <body style="background-color: lightgreen;">

                          <h1>DNA sequence</h1>

                            """ + DNAsequence + """

                                  </body>

                                  </html>

                                  """

            except KeyError:
                jsonvalue = 0
                HTTP_CODE = 404
                contents = """

                        <html>

                        <body style="background-color: lightblue;">

                        <h1>Invalid Name</h1>

                            </body>

                            </html>

                            """

        elif "/geneInfo" in self.path:
            keyandvalue = self.convert_dict(self.path)
            try:
                gene_name = keyandvalue['gene']
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                data1 = r1.read().decode('utf-8')
                conn.close()
                response = json.loads(data1)
                idd = response['data'][0]['id']
                ENDPOINT = "/overlap/id/" + idd + "?feature=gene;content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)

                r1 = conn.getresponse()
                data1 = r1.read().decode('utf-8')
                conn.close()
                response1 = json.loads(data1)
                start = response1[0]['start']
                end = response1[0]['end']
                length = end - start
                chromo = response1[0]['assembly_name']
                Features = {}
                Features['start'] = response1[0]['start']
                Features['end'] = response1[0]['end']
                Features['length'] = length
                Features['chromo'] = response1[0]['assembly_name']
                Features['id'] = idd

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Features)

                else:
                    jsonvalue = 0
                    contents = """

                                      <html>

                            <body style="background-color: lightgreen;">

                              <h1>Information about the Gene</h1>

                                """ + 'Start:' + str(start) + '\nEnd:' + str(end) + '\nLength:' + str(

                        length) + '\nChromosome:' + chromo + '\nId:' + idd + """

                                      </body>

                                      </html>

                                      """

            except KeyError:
                jsonvalue = 0
                HTTP_CODE = 404
                contents = """

                        <html>

                        <body style="background-color: lightblue;">

                        <h1>Invalid Name</h1>

                            </body>

                            </html>

                            """

        elif '/geneCal' in self.path:
            keyandvalue = self.convert_dict(self.path)

            try:
                gene_name = keyandvalue['gene']
                ENDPOINT = "/homology/symbol/human/" + gene_name + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                data1 = r1.read().decode('utf-8')
                conn.close()
                response = json.loads(data1)
                idd = response['data'][0]['id']
                ENDPOINT = "/sequence/id/" + idd + "?content-type=application/json"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                r1 = conn.getresponse()
                print('Response received: {}\n'.format(r1.status, r1.reason))

                data1 = r1.read().decode('utf-8')
                response = json.loads(data1)
                DNAsequence = response['seq']
                seq = Seq(DNAsequence)
                length = len(DNAsequence)
                perc_A = seq.perc('A')
                perc_C = seq.perc('C')
                perc_T = seq.perc('T')
                perc_G = seq.perc('G')

                Calculations = {}
                Calculations['length'] = length
                Calculations['Perc_A'] = perc_A
                Calculations['Perc_c'] = perc_C
                Calculations['Perc_T'] = perc_T
                Calculations['Perc_G'] = perc_G

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Calculations)

                else:
                    jsonvalue = 0
                    contents = """

                                      <html>

                            <body style="background-color: lightgreen;">

                              <h1>Total Lenght and Percentage of each Base</h1>

                                """ + 'Lenght' + str(length) + '<br>' + "Percentage of A's" + str(perc_A) + '<br>' + "Percentage of C's" + str(perc_C) + '<br>' + "Percentage of T's" + str(perc_T) + '<br>' + "Percentage of G's: " + str(perc_G) +\
                               """

                                      </body>

                                      </html>

                                      """

            except KeyError:
                jsonvalue = 0
                HTTP_CODE = 404
                contents = """

                        <html>

                        <body style="background-color: lightblue;">

                        <h1>Invalid Name</h1>

                            </body>

                            </html>

                            """

        elif "/geneList" in self.path:
            keyandvalue = self.convert_dict(self.path)
            try:
                chromo = keyandvalue['chromo']
                start = keyandvalue['start']
                end = keyandvalue['end']
                ENDPOINT = "/overlap/region/human/" + str(chromo) + ":" + str(start) + "-" + str(end) + "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT, None, headers)
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                conn.close()

                response2 = json.loads(data)
                stop = int(end) - int(start)
                count = 0
                List = []

                for possiblegene in response2:
                    if 'feature_type' in possiblegene and possiblegene['feature_type'] == 'gene':
                        List.append(possiblegene['external_name'])
                        count = count + 1

                        if count == stop:
                            break

                Dict = {}
                Dict['Gene'] = List

                if 'json=1' in self.path:
                    jsonvalue = 1
                    contents = json.dumps(Dict)

                else:
                    jsonvalue = 0
                    contents = """

                                                    <html>

                                          <body style="background-color: green;">

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

            except KeyError:
                jsonvalue = 0
                HTTP_CODE = 404
                contents = """

                                        <html>

                                        <body style="background-color: lightblue;">

                                        <h1>Invalid Name</h1>

                                            </body>

                                            </html>

                                            """

        else:
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
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()