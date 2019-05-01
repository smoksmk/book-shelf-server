class InternalError(Exception):
    def __init__(self, message=None, detail=None):
        self.code = 500
        self.message = message or 'Internal Error for service'
        self.detail = detail
