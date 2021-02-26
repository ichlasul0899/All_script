#!/usr/bin/env python3

import unittest

def validate_user(name, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True
  
  
class TestValidateUser(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(validate_user("Ichlasul Amal", 3), True)
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)
  # Test Nya emg ga lengkap cuma mewakilkan saja

unittest.main()
