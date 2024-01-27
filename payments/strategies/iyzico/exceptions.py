class CoreException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class CheckoutFormInitializeException(Exception):
    pass


class CheckoutFormRetrieveExeption(Exception):
    pass
