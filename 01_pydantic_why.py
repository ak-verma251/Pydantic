


# def insert_patient_data(name:str,age:int):

#   if type(name) == str and type(age) == int:
#      if age<0:
#         raise ValueError("Age cannot be negatice")
#      else:
#        print(name)
#        print(age)
#        print('inserted into data')
#   else:
#      raise TypeError('Incorrect data type')   

# def update_patient_data(name:str,age:int):

#   if type(name) == str and type(age) == int:
#      if age<0:
#         raise ValueError("Age cannot be negatice")
#      else:
#        print(name)
#        print(age)
#        print('inserted into data')
#   else:
#      raise TypeError('Incorrect data type') 
# 
# from numpy._core.defchararray import title
# from pydantic.json_schema import Examples
# from traitlets.utils import descriptions
from pydantic import BaseModel,EmailStr,AnyUrl, Field # used for custom data validation
from typing import List,Dict,Optional , Annotated

# by using field and annotated  we add metadata
 
class Patient(BaseModel):
  # name:str = Field(max_length = 50)
  name:Annotated[str,Field(max_length= 50), title :'Name of the patient',descriptions :'Give the name of the patient in less than 50 chars',Examples : ['NItish','ashish']]
  email:EmailStr
  age:int = Field(gt = 0, lt= 120)
  weight: float = Annotated[float, Field(gt =0,strict = True)]
  # married:bool = False
  married: Annotated[bool,Field(default=None), title :'Married',descriptions :'Marital status of the patient',Examples : [True,False]]
  allergies : Annotated[Optional[list[str]] , Field(default = None,max_length = 5)]
  contact_detail: dict[str,str]



def insertion_patient_data(patient:Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print(patient.contact_detail)
  print(patient.weight)

  print('inserted')


def update_patient_data(patient:Patient):
  print(patient.name)
  print(patient.age)
  print('inserted')

patient_info = {'name':'Ashish',
                'age':30,
                'weight':75.2,
                'married':True,
                # 'allergies':['pollen','dust'],
                'email':'patient@example.com',
                'contact_detail':{'phone':'0000000000'}
                }

patient1 = Patient(**patient_info) # double star is used for unpacking the dictionary

insertion_patient_data(patient1)
# update_patient_data(patient1)

