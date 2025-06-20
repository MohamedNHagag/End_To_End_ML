#تخصيص (Custom) لرسائل الخطأ في مشروع بايثون
#سجل الأخطاء بشكل مفصل ومنظم


#بدل ما يطلعلك الخطأ كده:
#ZeroDivisionError: division by zero
#هيطلعلك بالشكل ده:
#Error occured in python script name [main.py] line number [23] error message[division by zero]








import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys): #عرض تفاصيل دقيقة عن الخطأ 
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename #بيجيب اسم الملف اللي حصل فيه الخطأ.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) #بيرجع الرسالة المفصلة.تحتوي علي اسم الملف و رقم السطر ونص الخطا

    return error_message

    

class CustomException(Exception):  #ستخدام هذا الاستثناء في مشروعك بدلًا من Exception العادي، بحيث تكون الأخطاء أوضح وأسهل في تتبعها خاصة في اللوجات (logs).لعمل استثناء مخصص يحتوي على تلك التفاصيل.

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail) #نكوّن الرسالة التفصيلية باستخدام الدالة اللي فوق،
    
    def __str__(self):
        return self.error_message
    

