from .pricing_strategy import PricingStrategy

class LowSeasonStrategy(PricingStrategy):
  def calculate(self, base_price: float) -> float:
    return base_price * 0.80  # 20% de desconto

class HighSeasonStrategy(PricingStrategy):
  def calculate(self, base_price: float) -> float:
    return base_price * 1.20  # 20% de acréscimo