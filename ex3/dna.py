import random


class DNA:
    def __init__(self, seq):
        assert (self.check_correctness(seq))
        self.seq = seq
        print(f'Starting sequence {self.seq}')

    @classmethod
    def from_file(cls, file_name):

        with open(file_name, 'r') as f:
            dna_lines = f.readlines()

        # Taking only first sequence for test
        dna_seq = dna_lines[0].strip()

        return cls(dna_seq)

    def reverse(self):
        print(f'Reversed sequence {self.seq[::-1]}')

    def check_correctness(self, seq):
        nuc_set = set('ATCGN')

        return set(seq).issubset(nuc_set)

    def random_extend(self, number):
        extend_dna = random.choices(['A', 'T', 'C', 'G', 'N'], k=number)
        self.seq += ''.join(extend_dna)
        print(f'Extended sequence {self.seq}')

    def trimm(self, number):
        self.seq = self.seq[:-number]
        print(f'Trimmed sequence {self.seq}')

if __name__ == '__main__':

    dna_sq = 'ATGGGC'

    dna = DNA(dna_sq)

    dna.reverse()

    dna.random_extend(6)

    dna.trimm(6)

    dna = DNA.from_file('example_seq.txt')


