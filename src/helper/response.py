from typing import Any

from pydantic import BaseModel


class ResponseModel(BaseModel):
    """Creates a response model for the API.
    Structure which provides a static method for success or error response to the API.

    Attributes:
        status: The status of the response.
        message: The message of the response.
        data: The data of the response.
    """

    status: str
    message: str
    data: Any | None

    @staticmethod
    def success(message: str = "success", data: Any | None = None):
        """Provides a success response data
        Args:
            data (dict): data to be returned
            message (str, optional): Descriptive messaged. Defaults to "success".
        Returns:
            dict: key-value pair of status, message and data
        """

        return ResponseModel(status="success", message=message, data=data).dict()

    @staticmethod
    def error(message: str) -> dict[str, Any]:
        """Provides an error response data

        Args:
            data (dict): data to be returned
            detail (str): Descriptive error message.

        Returns:
            dict: key-value pair of status, detail
        """
        return ResponseModel(status="error", data={"detail": message}).dict()
