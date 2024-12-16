# from typing import Union

from fastapi import HTTPException

# class ExceptionDetail(HTTPException):
#     loc: list[Union[int, str]]
#     msg: str
#     type: str
#
# class ValidationException(HTTPException):
#     def __init__(self, detail: ExceptionDetail, status_code=422):
#         self.detail = detail
#         self.status_code = status_code

class PredictException(HTTPException):
    def __init__(self, msg: str, type: str = "error", status_code: int = 422):
        detail = [
            {
                "loc": ["model", "predict"],
                "msg": msg,
                "type": type,
            }
        ]
        super().__init__(status_code=status_code, detail=detail)