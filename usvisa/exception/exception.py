import os
import sys
import traceback

def error_message_details(error_message, error_details):
    """
    Function to extract details from the exception and format a detailed error message.
    """
    # Get the exception type, value, and traceback from the passed error_details tuple
    _, _, exc_tb = error_details
    
    # Get the file name, line number, and function name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    function_name = exc_tb.tb_frame.f_code.co_name
    
    # Format the detailed error message
    detailed_error_message = f"Error occurred in file: {file_name}, line: {line_number}, function: {function_name}\n"
    detailed_error_message += f"Error message: {error_message}\n"
    detailed_error_message += f"Traceback: {traceback.format_exc()}"
    
    return detailed_error_message
     

class usvisaException(Exception):
    def __init__(self, error_message, error_details=None):
        # Capture the current exception details if none are provided
        if error_details is None:
            error_details = sys.exc_info()
        
        # Correctly call the base class constructor with the error message
        super().__init__(error_message)
        
        # Generate the detailed error message using the provided function
        self.error_message = error_message_details(error_message, error_details)
        
    def __str__(self):
        # Return the detailed error message when the exception is raised
        return self.error_message



