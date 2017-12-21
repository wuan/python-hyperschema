from assertpy import assert_that
from mock import Mock

from hyperschema.link import Link


class TestLink(object):

    def setup(self):
        self.session = Mock()

    def test_get(self):
        response_mock = self.session.get()
        response_mock.status_code = 200
        response_mock.text = "{}"

        link = Link('http://host/path', session=self.session)

        link.follow()

        print(self.session)

        assert_that(self.session)
