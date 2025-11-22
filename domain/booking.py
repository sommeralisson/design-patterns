from strategies.pricing_strategy import PricingStrategy
from observers.observer import Observer
from typing import List

class Booking:
  def __init__(self, booking_id: str, room, strategy: PricingStrategy):
    self.id = booking_id
    self.room = room
    self.strategy = strategy # Strategy Injection
    self._observers: List[Observer] = []
    self.status = "PENDING"
    self.final_price = 0.0

  # --- Methods Strategy ---
  def set_strategy(self, strategy: PricingStrategy):
    """Permite a troca dinâmica da estratégia em tempo de execução."""
    self.strategy = strategy

  def calculate_total(self):
    base = self.room.get_base_price()
    self.final_price = self.strategy.calculate(base)
    return self.final_price

  # --- Methods Observer ---
  def attach(self, observer: Observer):
    self._observers.append(observer)

  def set_status(self, new_status: str):
    self.status = new_status
    self._notify_observers()

  def _notify_observers(self):
    for observer in self._observers:
      observer.update(self.status, self.id)