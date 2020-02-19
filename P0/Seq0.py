from pathlib import Path

def seq_ping():
    print("OK!")
seq_ping()

def seq_read_fasta(filename):

    """
    Read a file with a DNA sequence in FASTA format
    :param filename: String
    :return: String
    """

    # -- Read the file
    contents = Path(filename).read_text()

    # -- Remove the head
    body = contents.split('\n')[1:]

    # -- Return the body as a string
    return "".join(body)
