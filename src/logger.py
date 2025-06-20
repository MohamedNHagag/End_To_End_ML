# جديد كل مره بتشغل الكود ويتم تسجيل فيه الاحداث والمعلومات المهمه اثناء تنفيذ البرنامج. filelog انشاء





import logging  #مكتبة تسجيل الأخطاء والمعلومات
import os  #لإدارة المجلدات والمسارات 
from datetime import datetime  #علشان نستخدم التاريخ والوقت في ملف الوجو



LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #بيسمي ملف الوجو بتاريخ ووقت اللحظة دي     #ex )06_20_2025_05_30_12.log

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)