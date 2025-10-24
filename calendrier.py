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


def get_events(list_events: list) -> list:
    """
    Retourne la liste de tous les événements
    Returns:
        list: Liste des événements
    """
    return list_events


def get_sorted_events(list_events: list = events) -> list:
    """
    Retourne la liste des événements triés par ordre chronologique
    Returns:
        list: Liste des événements triés
    """
    return sorted(list_events, key=lambda param: param[0])


def get_first_event_name(list_events: list = events) -> str:
    """
    Retourne le nom du premier événement dans la liste
    Returns:
        str: Nom de l'événement ou None si la liste est vide
    """
    return list_events[0][2] if list_events else None
