class TransitionError(Exception):
  def __init__(self, previous, next_state, message):
      self.previous = previous
      self.next = next_state
      self.message = message
