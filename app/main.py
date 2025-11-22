import sys
import os

# Adiciona diretório raiz ao path para imports funcionarem
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from factory.room_factory import RoomFactory
from strategies.seasonal import LowSeasonStrategy, HighSeasonStrategy
from strategies.event import EventStrategy
from domain.booking import Booking
from observers.departments import ReceptionObserver, FinanceObserver
from infra.logger import Logger

def main():
  print("=== SISTEMA DE HOTELARIA ===")

  # 1. Factory Method: Criando quartos
  quarto_std = RoomFactory.create_room("standard", 101)
  quarto_lux = RoomFactory.create_room("luxo", 201)

  print(f"Criado: {quarto_std.get_description()} - Base: R${quarto_std.get_base_price()}")
  print(f"Criado: {quarto_lux.get_description()} - Base: R${quarto_lux.get_base_price()}")
  print("-" * 30)

  # 2. Strategy: Criando reserva com estratégia inicial (Baixa Temporada)
  reserva = Booking("RES-001", quarto_lux, LowSeasonStrategy())
  print(f"Reserva {reserva.id} criada na Baixa Temporada.")
  print(f"Valor calculado: R$ {reserva.calculate_total():.2f}")

  # Troca Dinâmica de Strategy (Runtime)
  print(">> Mudança de cenário: Chegou um grande Evento!")
  reserva.set_strategy(EventStrategy())
  print(f"Novo valor calculado: R$ {reserva.calculate_total():.2f}")
  print("-" * 30)

  # 3. Observer: Configurando observadores
  recepcao = ReceptionObserver()
  financeiro = FinanceObserver()

  reserva.attach(recepcao)
  reserva.attach(financeiro)

  # Mudança de estado dispara notificações
  print(">> Atualizando status para CONFIRMED:")
  reserva.set_status("CONFIRMED")

  print("\n>> Cliente não apareceu. Atualizando para NO-SHOW:")
  reserva.set_status("NO-SHOW")
  print("-" * 30)

  # 4. Singleton: Verificando logs
  print(">> Logs do Sistema (Infra Singleton):")
  for log in Logger().get_history():
    print(f"LOG: {log}")

  print("\n" + "="*30)
  print("Desenvolvido por: Alisson Sommer")
  print("="*30)

if __name__ == "__main__":
  main()