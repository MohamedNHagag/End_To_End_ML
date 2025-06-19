from setuptools import find_packages,setup #يجد جميع الحزم المتوفره بالكامل




from typing import List
# هذا المتغير يشير إلى السطر الذي لا نريده في requirements
dont_show='-e .'
# دالة لجلب المتطلبات من ملف requirements.txt
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path ,encoding='utf-8') as file_obg:
       requirements=file_obg.readlines()
       requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
       #requirements=[req.replace('\n',' ') for req in requirements ] 
       #if dont_show in requirements:
        #        requirements.remove(dont_show)
    return requirements




setup(
name='mlProject',
version='0.0.1',
author='Mohamedhagag',
author_email='hagag9868@gmail.com',
install_requires=get_requirements('requirements.txt'),
packages=find_packages()



#بتكتب بيانات وصفيه حول المشروع 

)