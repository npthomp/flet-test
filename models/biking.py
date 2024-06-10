from datetime import date
import pprint
import unittest

class Biking:
    program: str
    minutes: int
    level: int
    rpm: int
    calories: int
    when: date
    note: str

    def __init__(self, program: str, minutes: int, level: int, rpm: int, calories: int, when: date = date.today(), note:str = ""):
        self.program = program
        self.minutes = minutes
        self.level = level
        self.rpm = rpm
        self.calories = calories
        self.when = when
        self.note = note

    def __eq__(self, other):
        return all((
            self.program == other.program,
            self.minutes == other.minutes,
            self.level == other.level,
            self.rpm == other.rpm,
            self.calories == other.calories,
            self.when == other.when,
            self.note == other.note
        ))

    def to_dict(self):
        return {
            'program': self.program,
            'minutes': self.minutes,
            'level': self.level,
            'rpm': self.rpm,
            'calories': self.calories,
            'when': self.when.isoformat(),
            'note': self.note
        }
    
    @classmethod
    def from_dict(self, data: dict) -> "Biking":
        try:
            return Biking(
                program = data['program'],
                minutes = data['minutes'],
                level = data['level'],
                rpm = data['rpm'],
                calories = data['calories'],
                when = date.fromisoformat(data['when']),
                note = data['note']
            )
        except KeyError:
            raise ValueError("Invalid or incomplete data for a Biking record.\n{pprint.pformat(data)}")


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sample_biking = Biking("Cardio",30,10,70,400,date(2024,1,1),"test record")
        self.sample_dict = {
            'program': 'Cardio',
            'minutes': 30,
            'level': 10,
            'rpm': 70,
            'calories': 400,
            'when': '2024-01-01',
            'note': 'test record'
        }

    def test_to_dict(self):
        d = self.sample_biking.to_dict()
        self.assertEqual(d, self.sample_dict)

    def test_from_dict(self):
        d = Biking.from_dict(self.sample_dict)
        self.assertEqual(d, self.sample_biking)

    def test_to_dict_and_from_dict(self):
        biking = self.sample_biking
        d = biking.to_dict()
        biking2 = Biking.from_dict(d)
        self.assertEqual(biking, biking2)