class Seq:

    def __init__(self, strbases):



        self.strbases = strbases



    def get_sequence(self):

        return self.strbases



    def len(self):

        return len(self.strbases)



    def complement(self):



        D = {'A':'T','T':'A','C':'G','G':'C'}

        seq=[]



        for b in self.strbases:

            if b =='A':

                b=D[b]

                seq.append(b)

            elif b =='C':

                b=D[b]

                seq.append(b)

            elif b =='T':

                b=D[b]

                seq.append(b)

            elif b =='G':

                b=D[b]

                seq.append(b)

        trbases=''.join(seq)



        return Seq(trbases)



    def reverse(self):



        return Seq(self.strbases[::-1])



    def count(self, base):



        result = 0

        for basee in self.strbases:

            if basee == base:

                result += 1

        return result



    def perc(self, base):



        if len(base)>0:

            v=self.count(base)

            r=self.len()

            perc = round(100.0*v/r, 1)

            return perc

        else:

            perc = 0

            return perc
