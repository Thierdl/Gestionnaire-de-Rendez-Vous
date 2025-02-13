from django.test import TestCase
from .models import Appointement
from patient.models import Patient
from django.contrib.auth.models import User

from datetime import time,date

class TestAppointementModels(TestCase):
    def setUp(self):

        self.user=User.objects.create_user(
            email="albert@albert.sn",
            username="albert77",
            password="12345",
        )


        self.patient=Patient.objects.create(
            user=self.user,
            name="ndiaye",
            firstname="fanta",
            age=23,
            phone=77000
        )
        

        self.data_appoint=Appointement.objects.create(
            patient=self.patient,
            title="visite",
            date=date(2012, 12, 12),
            time=time(12, 12),
            place="dakar"

        )


    def test_content_appoint(self):
        self.assertEqual(self.data_appoint.patient.name, "ndiaye")
        self.assertEqual(self.data_appoint.title, "visite")
        self.assertEqual(self.data_appoint.date, date(2012, 12, 12))
        self.assertEqual(self.data_appoint.time, time(12, 12))
        self.assertEqual(self.data_appoint.place, "dakar")
        