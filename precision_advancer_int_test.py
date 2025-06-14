# --------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test Precision advancer with integer vales
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --------------------------------------------------

import unittest
import precision_advancer_int as pai

class TestPrecision(unittest.TestCase):

# --------------------------------------------------
  def test_to_int(self):
    expected = (123, -2)
    actual = pai.to_int(1.23)
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_from_int(self):
    expected = 12.34
    actual = pai.from_int((1234, -2))
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_dec_to_int(self):
    @pai.dec_to_int
    def add(x, y):
      return x+y

    expected = (12, -1)
    actual = add(0.7, 0.5)
    self.assertEqual(expected, actual)
  
# --------------------------------------------------
  def test_dec_from_int(self):
    @pai.dec_from_int
    def add(x, y):
      return (pai.to_int(x+y))

    expected = 1.2
    actual = add(0.7, 0.5)
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_sm_factor(self):
    lst = [(12, -3), (1234, -4)]
    expected = -4
    actual = pai.__sm_factor__(lst)
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_refactor(self):
    lst = [(12, -3), (1234, -4)]
    expected = [(120, -4), (1234, -4)]
    actual = pai.__refactor__(lst)
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_add(self):
    expected = (540, -2)
    actual = pai.add((4, -1), (500, -2))
    self.assertEqual(expected, actual)
    
# --------------------------------------------------
  def test_sub(self):
    expected = (40, -2)
    actual = pai.sub((54, -1), (500, -2))
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_mul(self):
    expected = (12, -3)
    actual = pai.mul((2, -2), (6, -1))
    self.assertEqual(expected, actual)

# --------------------------------------------------
  def test_div(self):
    expected = (3, -3)
    actual = pai.div((12, -4), (4, -1))
    self.assertEqual(expected, actual)

# --------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# End of file
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --------------------------------------------------

