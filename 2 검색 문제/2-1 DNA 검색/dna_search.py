from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # 코돈 타입 앨리어스
Gene = List[Codon]


gene_str: str = "ACGTGGCTCTCTCTAACGTACGTACGTACGGGTTTAAA"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        # 3개의 뉴클레오타이드에서 코돈을 초기화
        codon: Codon = (Nucleotide[s[i]],
                        Nucleotide[s[i+1]],
                        Nucleotide[s[i+2]],
                        )
        gene.append(codon)
    return gene


my_gene: Gene = string_to_gene(gene_str)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True

    return False


my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
