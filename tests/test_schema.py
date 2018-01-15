from assertpy import assert_that

from hyperschema.schema import Schema


class TestSchema(object):

    def test_get_of_non_existent_rel(self):
        empty_schema = Schema()

        result = empty_schema.follow('any')

        assert_that(result.data).is_empty()
        assert_that(result.schema.links).is_empty()
