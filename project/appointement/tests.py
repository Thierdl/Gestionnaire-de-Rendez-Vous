from django.test import TestCase
from django.contrib.auth.models import User
from .models import Appointement
from patient.models import Patient
from datetime import date, time


class TestAppointement(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(
            username="albert",
            email="contact@albert.sn",
            password="12345",
        )

        self.patient=Patient.objects.create(
            user=self.user,
            name="mane",
            firstname="moussa",
            age=23,
            phone=770778899

        )

    def test_content_app(self):

        data_appointement=Appointement.objects.create(
            patient=self.patient,
            title="visite",
            date=date(2025, 2, 14),
            time=time(12, 12)
        )


        self.assertEqual(data_appointement.patient.user.username, "albert")
        self.assertEqual(data_appointement.title, "visite")
        self.assertEqual(data_appointement.date, date(2025, 2, 14))
        self.assertEqual(data_appointement.time, time(12, 12))


    def test_update_app(self):
        appointement=Appointement.objects.create(
            patient=self.patient,
            title="diner",
            date=date(2020, 4, 27),
            time=time(8, 0),
            place="fastfood"
        )

        new_title="thierdl"
        new_date=date(1945, 6, 20)
        new_time=time(9, 0)
        new_place="zig"

        appointement.title=new_title
        appointement.date=new_date
        appointement.time=new_time
        appointement.place=new_place
        
        appointement.save()

        dataapp=Appointement.objects.get(id=appointement.id)

        
        self.assertEqual(dataapp.title, dataapp.title)
        self.assertEqual(dataapp.date, dataapp.date)
        self.assertEqual(dataapp.time, dataapp.time)
        self.assertEqual(dataapp.place, dataapp.place)


    def test_del_app(self):
        appointement=Appointement.objects.create(
                patient=self.patient,
                title="soire",
                date=date(2025, 3, 25),
                time=time(12, 23),
                place="ngor",
        )
        
        self.assertEqual(Appointement.objects.count(), 1)

        appointement.delete()

        self.assertEqual(Appointement.objects.count(), 0)