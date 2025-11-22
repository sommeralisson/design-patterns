class Logger:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Logger, cls).__new__(cls)
      cls._instance.logs = []
    return cls._instance

  def log(self, message: str):
    self.logs.append(message)

  def get_history(self):
    return self.logs