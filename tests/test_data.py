from assertpy import assert_that
from mock import Mock, call

from hyperschema.data import Data


class TestData(object):

    def test_data_get_item(self):
        data = Data({'foo': 'bar'})

        assert_that(data['foo']).is_equal_to('bar')

    def test_data_is_empty(self):
        data = Data()

        assert_that(data.is_empty()).is_true()

    def test_data_is_not_empty(self):
        data = Data({'foo': 'bar'})

        assert_that(data.is_empty()).is_false()

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

        assert_that(result.data).is_empty()
        assert_that(result.schema.links).is_empty()


class TestListData(object):

    def test_data_get_item(self):
        data = Data({'foo': 'bar'})

        assert_that(data['foo']).is_equal_to('bar')
