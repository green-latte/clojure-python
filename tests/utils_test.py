import unittest

from oneway import utils as _


class UnderscoreTest(unittest.TestCase):
  def setUp(self):
    self.arr = [1, 'a', [2, 'b'], {'c': 3}, None]

  def test_some_and_every(self):
    is_str = lambda x: type(x) == str
    self.assertTrue(_.some(self.arr, is_str))
    self.assertTrue(not _.every(self.arr, is_str))

  def test_first_and_rest(self):
    self.assertEqual(_.first(self.arr), 1)
    self.assertEqual(_.rest(self.arr), ['a', [2, 'b'], {'c': 3}, None])

  def test_contains_and_has(self):
    self.assertTrue(self.arr, [2, 'b'])
    lastSecond = _.compose(_.first, _.rest, _.reverse)
    obj = lastSecond(self.arr)
    self.assertTrue(_.has(obj, 'c'))

  def test_bind_and_all(self):
    pass

  def test_chain(self):
    pass

  def test_compose(self):
    lastSecond = _.compose(_.first, _.rest, _.reverse)
    obj = lastSecond(self.arr)
    self.assertEqual(obj, {'c': 3})

  def test_each(self):
    result = []
    def f(x, i):
      result.append(x is None)
    _.each(self.arr, f)
    falsy = _.compose(_.isNot, _.truthy)
    self.assertTrue(_.some(result, falsy))

  def test_group_index_count_by(self):
    pass

  def test_find(self):
    idx = _.find(self.arr, lambda v, i, a: type(v) == str)
    self.assertEqual(idx, 'a')
