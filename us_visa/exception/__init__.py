import os
import sys
from typing import Type

def error_message_detail(error: Exception, error_detail: Type[sys]) -> str:
    """
    Constructs a detailed error message including script name, line number, and error message.
    
    :param error: The Exception object raised
    :param error_detail: The sys module to get exception details
    :return: Formatted error message string
    """
    # Get the traceback object from the sys module
    _, _, exc_tb = error_detail.exc_info()
    # Extract the filename and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    # Construct the error message
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"

    return error_message

class USvisaException(Exception):
    def __init__(self, error_message: str, error_detail: Type[sys]):
        """
        Custom exception class for handling exceptions with detailed error messages.
        
        :param error_message: Error message in string format
        :param error_detail: The sys module to get exception details
        """
        super().__init__(error_message)
        # Generate the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        # Return the detailed error message when the exception is printed
        return self.error_message
