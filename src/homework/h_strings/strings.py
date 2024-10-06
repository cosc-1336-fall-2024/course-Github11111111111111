#Homework 5
def get_hamming_distance(dna1, dna2): 

    Lan = len(dna1)

    distance = 0 

    for i in range(Lan):
        if dna1[i] != dna2[i]: 
            distance += 1

    return distance
    
def get_dna_complement(dna):

    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    reverse_complement = ""

    for index in range(0, len(dna)):
        base = dna[index]
        reverse_complement += complement[base]

    result_complement = reverse_complement[::-1]

    return result_complement