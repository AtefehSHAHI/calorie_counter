class InvalidItems(Exception):
    def __init__(self, item):
        message = f"Error: '{item}' is not in any menus."  
        super().__init__(message)

class TooMuchCalories(Exception):
    def __init__(self):
        message = f"Error: The order has more than 2000 calories"  
        super().__init__(message)