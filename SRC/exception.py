import sys


def error_message_details(error,error_detail:sys):
    exc_type,exc_value,exc_traceback=error_detail.exc_info()
    file_name=exc_traceback.tb_frame.f_code.co_filename

    error_message="error occur in application script name[{0}],line no [{1}],and error masse is[{2}]".format(
        file_name,exc_traceback.tb_lineno,str(error)
    )
    return error_message


class Custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    