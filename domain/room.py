from abc import ABC, abstractmethod

class Room(ABC):
  def __init__(self, number):
    self.number = number

  @abstractmethod
  def get_base_price(self) -> float:
    pass

  @abstractmethod
  def get_description(self) -> str:
    pass

class StandardRoom(Room):
  def get_base_price(self) -> float:
    return 100.00

  def get_description(self) -> str:
    return f"Quarto Standard #{self.number}"

class LuxuryRoom(Room):
  def get_base_price(self) -> float:
    return 250.00

  def get_description(self) -> str:
    return f"Suíte Luxo #{self.number} (com vista mar)"