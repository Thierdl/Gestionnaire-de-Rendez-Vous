from django.test import TestCase
from django.contrib.auth.models import User
from .models import Patient


class TestPatientModels(TestCase):
    def setUp(self):
      #creer un user
      self.user = User.objects.create_user(
                        email="albert@albert.sn", 
                        username="albert", 
                        password="12345"
                        
                        )

      #creer un article
      self.data_patient = Patient.objects.create(
                        
                        user=self.user,
                        name="xarala",
                        firstname="xarala2025",
                        age=23,
                        phone=770778899,

                        )

    def test_content_article(self):
        self.assertEqual(self.data_patient.user.email, "albert@albert.sn")
        self.assertEqual(self.data_patient.name, "xarala")
        self.assertEqual(self.data_patient.firstname, "xarala2025")
        self.assertEqual(self.data_patient.age, 23)
        self.assertEqual(self.data_patient.phone, 770778899)
