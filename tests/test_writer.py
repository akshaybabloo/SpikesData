from numpy.testing import TestCase, assert_array_equal, run_module_suite, assert_
import numpy as np
import os
from spikesparser.reader import ReadCSV

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestCSVReader(TestCase):
    """
    Testing ``ReadCSV`` object.
    """

    def setUp(self):
        self.data_location = os.path.join(BASE_DIR, 'data')
        self.read_csv_object = ReadCSV(self.data_location)

        self.init_data = np.asarray([
            [
                [60.9714878, 60.70771189, 63.67634345, 68.34706252, 36.65221366],
                [22.0331885, 59.90428826, 22.24081467, 26.49077798, 67.15344005],
                [43.42420744, 21.39717261, 21.5964398, 50.58231716, 53.88228669],
                [56.3882456, 64.49245047, 33.62847541, 69.62686169, 27.66015559],
                [42.67148085, 42.57732552, 56.69777865, 45.80885181, 39.36014037]
            ],
            [
                [42.46760853, 43.38494825, 43.16139244, 61.09694826, 43.71462622],
                [35.83176163, 40.15718186, 61.42337428, 67.20076627, 66.00662776],
                [34.11933193, 65.91810143, 21.55806121, 25.35323117, 67.44497639],
                [57.08793485, 51.40662274, 51.02275454, 35.67353513, 26.28231511],
                [26.86046066, 57.80954537, 38.45369823, 29.03152157, 48.5931396]
            ]
        ])

    def test_read_samples(self):
        """
        Tests ``read_samples()``
        """

        assert_array_equal(self.read_csv_object.read_samples(), self.init_data)

    def test_sample_size(self):
        """
        Tests ``sample_size()``
        """

        assert_array_equal(self.read_csv_object.sample_size(), np.shape(self.init_data)[0])


if __name__ == '__main__':
    run_module_suite()
