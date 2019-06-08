class ResponseError(Exception):
    def __init__(self, name, message):
        msg = "{}({})".format(message, name)
        super().__init__(msg)


class ValidationError(ResponseError):
    pass


class OrderNotFoundError(ResponseError):
    pass


class WithdrawAddressNotRegisteredError(ResponseError):
    pass


class WithdrawInsufficientBalanceError(ResponseError):
    pass


class UnknownServerError(ResponseError):
    pass


def find_error_types(name):
    switcher = {
        'validation_error': ValidationError,
        'order_not_found': OrderNotFoundError,
        'withdraw_address_not_registered': WithdrawAddressNotRegisteredError,
        'withdraw_insufficient_balance': WithdrawInsufficientBalanceError,
        'server_error': UnknownServerError,
    }
    return switcher.get(name, ResponseError)
