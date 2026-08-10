from Bio.SeqUtils import MeltingTemp as mt

def calculate_tm(secuencia: str) -> float:
    """
    Calcula la Temperatura de Fusión (Tm) usando la regla de Wallace.
    Ideal para primers cortos (14-20 nucleótidos).
    """
    # mt.Tm_Wallace aplica internamente la fórmula matemática
    tm_value = mt.Tm_Wallace(secuencia)
    return float(tm_value)
