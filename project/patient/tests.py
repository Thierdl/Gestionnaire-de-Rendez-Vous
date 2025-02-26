from django.test import TestCase
from django.contrib.auth.models import User
from .models import Patient
from django.urls import reverse


class TestPatientModels(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(
                    email="albert@albert.sn", 
                    username="albert", 
                    password="12345"
                    
                    )

    

  def test_content_patient(self):
      
    data_patient = Patient.objects.create(
                    
                    user=self.user,
                    name="xarala",
                    firstname="xarala2025",
                    age=23,
                    phone=770778899,

                    )
    
    self.assertEqual(data_patient.user.email, "albert@albert.sn")
    self.assertEqual(data_patient.name, "xarala")
    self.assertEqual(data_patient.firstname, "xarala2025")
    self.assertEqual(data_patient.age, 23)
    self.assertEqual(data_patient.phone, 770778899)





  def test_upd_patient(self):
    patient=Patient.objects.create(
                    user=self.user,
                    name='albert', 
                    firstname='albert410',
                    age=22,
                    phone=77000,
                    )
      

    new_name="gamal"
    new_firstname="camilla"
    new_age=24
    new_phone=221

    new_user=User.objects.create_user(
                  username="moussa", 
                  email="contact@moussa.sn", 
                  password="123456"
                  )
    

    patient.name=new_name
    patient.firstname=new_firstname
    patient.age=new_age
    patient.phone=new_phone
    patient.user=new_user

    patient.save()

    upd_patient=Patient.objects.get(id=patient.id)



    self.assertEqual(upd_patient.name, new_name)
    self.assertEqual(upd_patient.firstname, new_firstname)
    self.assertEqual(upd_patient.age, new_age)
    self.assertEqual(upd_patient.phone, new_phone)
    self.assertEqual(upd_patient.user, new_user)



  def test_del_patient(self):
    patient=Patient.objects.create(
                  user=self.user,
                  name="xarala",
                  firstname="xarala2025",
                  age=23,
                  phone=770778899,

    )

    self.assertEqual(Patient.objects.count(), 1)

    patient.delete()

    self.assertEqual(Patient.objects.count(), 0)

