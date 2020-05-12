import socket
import termcolor
import pathlib



# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "yellow")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # in order to read the file properly a new function is defined,
    # it has the same purpose as the seq_read_fasta() defined in the practice 1

    def read_file(FILENAME):
        #first we need to open and read the desired file
        contents = pathlib.Path(FILENAME).read_text().split("\n")[1:]  # Split lines and skip the first one [1:]
        body = "".join(contents)  # Return the body as a string without the \n characters (without spaces)
        return body

    FOLDER = "../P4/"

    request = req_line.split(" ")[1]
    # request is like req_line (GET /info/A HTTP/1.1) only with (/info/A)
    if "/" == request:
        body = read_file(FOLDER + "index.html")
    elif "/info/C" == request:  # req_line is GET /info/A HTTP/1.1
        body = read_file(FOLDER + "C.html") #if what we are requesting is /info/A the program will return the html A file

    elif "/info/A" == request:  # req_line is GET /info/A HTTP/1.1
        body = read_file(FOLDER + "A.html")

    elif "/info/G" == request:  # req_line is GET /info/A HTTP/1.1
        body = read_file(FOLDER + "G.html")

    elif "/info/T" == request:  # req_line is GET /info/A HTTP/1.1
        body = read_file(FOLDER + "T.html")

    else:
        body = read_file(FOLDER + "ERROR.html") # if what we are requesting is other thing, the program will return the error page

    # we "create" each part of the response message and then join them together
    # 1) Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # 2) Add the Content-Type header
    header = "Content-Type: text/html\n"

    # 3) Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # 4) Build the message by joining together all the parts
    response_msg = status_line + header + "\r\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # Close the socket
        cs.close()