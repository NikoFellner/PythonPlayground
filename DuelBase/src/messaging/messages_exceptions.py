class HeroDied(Exception):
    """Raised when the hero dies."""

    def __init__(self, message: str = "The hero has died."):
        super().__init__(message)
