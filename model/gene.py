from dataclasses import dataclass


@dataclass
class Gene:
    id: int
    funzione: str
    essenziale:str
    cromosoma:int


    def __str__(self):
        return f'{self.id}{self.funzione} {self.essenziale} {self.cromosoma}'
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id

