# Stubs for bs4.tests.test_html5lib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from bs4.testing import HTML5TreeBuilderSmokeTest, SoupTest

HTML5LIB_PRESENT: bool

class HTML5LibBuilderSmokeTest(SoupTest, HTML5TreeBuilderSmokeTest):
    @property
    def default_builder(self): ...
    def test_soupstrainer(self) -> None: ...
    def test_correctly_nested_tables(self) -> None: ...
    def test_xml_declaration_followed_by_doctype(self) -> None: ...
    def test_reparented_markup(self) -> None: ...
    def test_reparented_markup_ends_with_whitespace(self) -> None: ...
    def test_reparented_markup_containing_identical_whitespace_nodes(self) -> None: ...
    def test_reparented_markup_containing_children(self) -> None: ...
    def test_processing_instruction(self) -> None: ...
    def test_cloned_multivalue_node(self) -> None: ...
    def test_foster_parenting(self) -> None: ...
    def test_extraction(self) -> None: ...
    def test_empty_comment(self) -> None: ...
