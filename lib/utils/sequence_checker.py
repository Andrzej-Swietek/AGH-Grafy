from typing import List

class SequenceChecker:
    @staticmethod
    def is_graphic(sequence: List[int]) -> bool:
        """
        Sprawdza, czy podana sekwencja jest sekwencją graficzną. False dla pustej sekwencji.
        """
        if not sequence:
            return False
        
        if sum(sequence) % 2:
            return False
            
        seq = sequence.copy()
        seq.sort(reverse=True)
        
        while True:
            if all(x == 0 for x in seq):
                return True
            if seq[0] >= len(seq) or any(x < 0 for x in seq):
                return False
            i=1
            while i <= seq[0]:
                seq[i] -= 1
                i += 1
            seq[0] = 0
            seq.sort(reverse=True)
        