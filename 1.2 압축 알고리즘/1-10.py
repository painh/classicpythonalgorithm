from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b010
            elif nucleotide == "T":
                self.bit_string |= 0b011
            else:
                raise ValueError(f"유효하지 않은 뉴클레오타이드입니다.{nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"invalid bits{bits}")
        return gene[::-1]  # [::-1]은 문자열을 뒤집는다

    def __str__(self) -> str:
        return self.decompress()


original: str = "TAGGGATTAACCGTTATATATATATAACCCGGAA" * 100
print(f"원본: {getsizeof(original)}")
compressed: CompressedGene = CompressedGene(original)
print(f"압축: {getsizeof(compressed.bit_string)}")
print(compressed)  # decompress
print(f"원본 문자열과 압축 해제한 문자열은 같습니까? {original == compressed.decompress()}")
