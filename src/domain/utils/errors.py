from http import HTTPStatus


class BusinessException(Exception):
    def __init__(
        self,
        message: str,
        status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
        *args
    ) -> None:
        super().__init__(message, *args)
        self.status_code = status_code
