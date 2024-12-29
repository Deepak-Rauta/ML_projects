import sys

def error_message_details(error, error_detail:sys): # when error occurs i raise my own custome message i.e error, error_detail was present inside the sys
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # was present inside custom exception handling Documentations
    error_message = "Error Occured in Pyhton scripts name [{0}] line number [{1}] error message [{2}]".format(
         file_name, exc_tb.tb_lineno, str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message



