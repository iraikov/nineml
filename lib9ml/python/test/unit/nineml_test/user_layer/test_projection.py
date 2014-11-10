import os.path
import unittest
from nineml import read
from nineml.user_layer import Projection


class TestPopulation(unittest.TestCase):

    def test_load(self):
        context = read(os.path.join(os.path.dirname(__file__), '..', '..',
                                    '..', '..', '..', '..', 'examples', 'xml',
                                    'projections',  'simple.xml'))
        self.assertEquals(type(context['Izhikevich2HH']), Projection)
