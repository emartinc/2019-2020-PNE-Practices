import socket
from Seq1 import Seq
import termcolor

IP = "127.0.0.1"
PORT = 8080
seq = ["AGTGGCGATGCGTAGGGCTGCGGATGGACACCAGTGGAAACGGT","AAAGGCTGGACCCAGATGACATTTAGCAGAT",
       "GGGATGCACCAGTAGAAACAGTAGACCCAGATAGGACAGTAGCAG","GATGAGGGGAGATAGGGAGAGGAGACAGAT",
       "TGGCGGTGAACCAAAATGCCATCAGG"]
# Server
# Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Preventing the error: "Port already in use" THIS IS OPTIONAL
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))  # Socket's IP and PORT with .bind() method

# Become a listening socket
ls.listen()
# MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()

    else:
        # Receive the message
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        try:
            msg_info = msg.split(" ")  # split the msg "GET 1" into ["GET","1"]
            service = msg_info[0]  # For example GET
            seq1 = msg_info[1]  # 1 , 2

        except IndexError:
            service = msg

    # PING command
        if "PING" == service:
            response = "OK!\n"  # Return response OK!!

        # GET command
        elif "GET" == service:
            response = seq[int(seq1)]

        elif "INFO" == service:
            seq_info = Seq(seq1)  # seq1 is the sequence
            count_bases_string = ""

            for base, count in seq_info.count().items():
                s_base = str(base) + ": " + str(count) + " (" + str(
                    round(count / seq_info.len() * 100, 2)) + "%)" + "\n"
                count_bases_string += s_base

            response = ("Sequence: " + str(seq_info) + "\n" +
                        "Total length: " + str(seq_info.len()) + "\n" +
                        count_bases_string)

        elif "COMP" == service:
            complementary = Seq(seq1)
            response = complementary.complement() + "\n"

        elif "REV" == service:
            reverse= Seq(seq1)
            response = reverse.reverse() + "\n"

        elif "GENE" == service:
            gene = seq1
            s = Seq()
            s.read_fasta("../Session-04/" + gene + ".txt")
            response = str(s) + "\n"

    # Server Console

    termcolor.cprint(f'{service}', "green")
    print(response)

    # Client console

    cs.send(response.encode())  # Encode the message and send message
    # Close
    cs.close()