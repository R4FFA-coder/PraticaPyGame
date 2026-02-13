from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, surf, rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    @abstractmethod
    def move(self) -> None:
        pass