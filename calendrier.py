from datetime import datetime

# Liste pour stocker les événements
events = []


def create_event(T1: datetime, t: int, n: str) -> tuple:
    """
    Crée un nouvel événement
    Args:
        T1 (datetime): Date et heure de début de l'événement
        t (int): Durée en secondes
        n (str): Nom de l'événement
    Returns:
        tuple: (timestamp_début, durée, nom)
    """
    event = (T1, t, n)
    events.append(event)
    return event
