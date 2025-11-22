from abc import ABC, abstractmethod

class Observer(ABC):
  @abstractmethod
  def update(self, status: str, booking_id: str):
    pass