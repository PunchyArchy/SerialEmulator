import unittest
from scale_emulator.main import SerialEmulator


class TestCase(unittest.TestCase):
    inst = SerialEmulator(data_source='real_data.txt')

    def test_main(self):
        self.inst.main()


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
