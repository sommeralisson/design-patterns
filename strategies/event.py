from .pricing_strategy import PricingStrategy

class EventStrategy(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price * 1.50  # 50% de acréscimo