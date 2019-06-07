class ResponseError(Exception):
    def __init__(self, name, message):
        msg = "{}({})".format(message, name)
        super().__init__(msg)
