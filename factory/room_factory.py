from domain.room import StandardRoom, LuxuryRoom, Room

class RoomFactory:
  @staticmethod
  def create_room(room_type: str, number: int) -> Room:
    if room_type.lower() == "standard":
      return StandardRoom(number)
    elif room_type.lower() == "luxo":
      return LuxuryRoom(number)
    else:
      raise ValueError("Tipo de quarto desconhecido.")