import unittest
from domain.booking import Booking
from domain.room import StandardRoom
from strategies.seasonal import LowSeasonStrategy, HighSeasonStrategy
from factory.room_factory import RoomFactory
from infra.logger import Logger
from observers.observer import Observer

class TestPatterns(unittest.TestCase):

  def setUp(self):
    # Limpa o singleton antes de cada teste
    Logger._instance = None

  def test_strategy_dynamic_switching(self):
    """Prova que mudar a estratégia altera o cálculo em tempo de execução."""
    room = StandardRoom(100) # Preço base 100
    booking = Booking("TEST-1", room, LowSeasonStrategy())

    # Baixa temporada: 100 * 0.8 = 80
    self.assertEqual(booking.calculate_total(), 80.0)

    # Troca dinâmica para Alta Temporada
    booking.set_strategy(HighSeasonStrategy())
    # Alta temporada: 100 * 1.2 = 120
    self.assertEqual(booking.calculate_total(), 120.0)

  def test_factory_creation(self):
    """Prova que a Factory cria instâncias corretas baseadas em parâmetros."""
    r1 = RoomFactory.create_room("standard", 1)
    r2 = RoomFactory.create_room("luxo", 2)

    self.assertIsInstance(r1, StandardRoom)
    self.assertEqual(r1.get_base_price(), 100.0)
    self.assertEqual(r2.get_base_price(), 250.0)

  def test_observer_notification(self):
    """Prova que observadores são notificados na mudança de estado."""
    class MockObserver(Observer):
      def __init__(self):
        self.notified = False
        self.last_status = None

      def update(self, status, booking_id):
        self.notified = True
        self.last_status = status

    booking = Booking("TEST-OBS", StandardRoom(100), LowSeasonStrategy())
    mock_obs = MockObserver()
    booking.attach(mock_obs)

    booking.set_status("CHECK-IN")

    self.assertTrue(mock_obs.notified)
    self.assertEqual(mock_obs.last_status, "CHECK-IN")

  def test_singleton_uniqueness(self):
    """Prova que múltiplas chamadas ao Logger retornam a mesma instância."""
    l1 = Logger()
    l2 = Logger()

    l1.log("Teste")

    self.assertIs(l1, l2) # Mesma referência de memória
    self.assertIn("Teste", l2.get_history()) # Estado compartilhado

if __name__ == '__main__':
  unittest.main()