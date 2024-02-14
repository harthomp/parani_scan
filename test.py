import unittest
import parani

# WARNING TESTS ARE NOT WRITTEN WELL 

class TestClass(unittest.TestCase):
    parani_dev = parani.Parani_SD1000()

    def test_serial_connection(self):
        self.assertTrue(self.parani_dev.serial_line.is_open)

    def test_bt_info(self):
        self.parani_dev.bt_info()
        self.assertIn(b"OK", self.parani_dev.response)
    
    def test_bt_inq(self):
        self.parani_dev.bt_inq()
        self.assertIn(b"**UNKNOWN**", self.parani_dev.response)
    
    # This test will fail if the device is not in a PENDING operational state.
    def test_bt_cancel(self):
        self.parani_dev.bt_cancel()
        self.assertIn(b"OK", self.parani_dev.response)

    #def test_bt_mode(self):
    #    self.parani_dev.bt_mode(3)
    #    self.assertIn(b"OK", self.parani_dev.response)

    # Will fail if the status is not in pending state - i.e. is not in bad state
    #def test_atz(self):
    #    self.parani_dev.atz()
    #    self.assertIn(b"OK", self.parani_dev.response)

if __name__ == "__main__":
    unittest.main()
