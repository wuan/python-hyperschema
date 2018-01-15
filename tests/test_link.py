from assertpy import assert_that
from mock import Mock, call

from hyperschema.link import Link


class TestLink(object):

    def setup(self):
        self.session = Mock()

    def test_get_with_empty_response(self):
        response_mock = self.session.get()
        response_mock.status_code = 200
        response_mock.text = "{}"

        link = Link('http://host/path', session=self.session)

        result = link.follow()

        assert_that(self.session.get.call_args).is_equal_to(call('http://host/path'))
        assert_that(result.data).is_empty()
        assert_that(result.schema.links).is_empty()
