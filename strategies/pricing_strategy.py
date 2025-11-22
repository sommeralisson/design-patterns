from abc import ABC, abstractmethod

class PricingStrategy(ABC):
  """Interface para estratégias de precificação."""

  @abstractmethod
  def calculate(self, base_price: float) -> float:
    pass