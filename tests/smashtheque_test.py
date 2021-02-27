import pytest

from smashtheque.smashtheque import Smashtheque

def test_smashtheque_init():
  o = Smashtheque(None, 'mytoken')
  assert isinstance(o, Smashtheque)
