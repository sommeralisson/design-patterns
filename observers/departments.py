from .observer import Observer
from infra.logger import Logger

class ReceptionObserver(Observer):
  def update(self, status: str, booking_id: str):
    msg = f"[RECEPÇÃO] Notificada: Reserva {booking_id} mudou para '{status}'. Preparar chaves."
    print(msg)
    Logger().log(msg)

class FinanceObserver(Observer):
  def update(self, status: str, booking_id: str):
    if status == "NO-SHOW":
      msg = f"[FINANCEIRO] Alerta: Reserva {booking_id} é No-Show. Aplicar multa."
      print(msg)
      Logger().log(msg)
    elif status == "CONFIRMED":
      msg = f"[FINANCEIRO] Reserva {booking_id} confirmada. Verificar pré-pagamento."
      print(msg)