from assertpy import assert_that

from hyperschema.schema import Schema


class TestSchema(object):

    def test_get_of_non_existent_rel(self):
        empty_schema = Schema()

        result = empty_schema.follow('any')

        assert_that(result.data).is_empty()
        assert_that(result.schema.links).is_empty()

    def test_creation_of_schema(self):

        links_node = [
            {
                'rel': '<rel>',
                'href': '<href>',
                'method': '<method>',
                'schema': '<schema>',
                'targetSchema': '<targetSchema>'
            }
        ]

        schema = Schema(links_node)

        link = schema.show('<rel>')

        assert_that(link.href).is_equal_to('<href>')
        assert_that(link.method).is_equal_to('<method>')
        assert_that(link.schema).is_equal_to('<schema>')
        assert_that(link.target_schema).is_equal_to('<targetSchema>')
