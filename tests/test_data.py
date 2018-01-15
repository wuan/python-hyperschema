from assertpy import assert_that
from mock import Mock, call

from hyperschema.data import Data


class TestData(object):

    def test_data_get_item(self):
        data = Data({'foo': 'bar'})

        assert_that(data['foo']).is_equal_to('bar')

    def test_empty_data_is_not_valid(self):
        data = Data()

        assert_that(data.is_valid()).is_false()

    def test_data_is_valid(self):
        data = Data({})

        assert_that(data.is_valid()).is_true()

    def test_data_follow(self):
        schema = Mock()
        data = Data(None, schema)
        payload = {'bar': 'baz'}

        result = data.follow('foo', payload)

        assert_that(schema.follow.call_args).is_equal_to(call('foo', payload))
        assert_that(schema.follow.return_value).is_equal_to(result)

    def test_get_of_non_existent_rel(self):
        empty_data = Data()

        result = empty_data.follow('any')

        assert_that(result.data).is_none()
        assert_that(result.schema.links).is_empty()

    def test_empty_data_has_empty_iterator(self):
        empty_data = Data()

        data = [value for value in empty_data]

        assert_that(data).is_empty()

    def test_data_iterator_should_fail(self):
        data = Data({'foo': 'bar'})

        iterated_data = [value for value in data]

        assert_that(iterated_data).contains_only('foo')

class TestListData(object):

    def test_data_get_item(self):
        data = Data({'foo': 'bar'})

        assert_that(data['foo']).is_equal_to('bar')
