import textwrap

from markdown import Markdown
from mdx_alerts import AlertExtension


def test_basic_conversion() -> None:
    """Test the basic conversion without additional parameters."""
    # given
    md = Markdown(extensions=[AlertExtension()])
    pattern = textwrap.dedent(
        """
        :: info
        This is the body.

        Even multi-line is possible.
        ::
        """
    )
    expected = textwrap.dedent("""\
        <div class="alert alert-info" role="alert">
        <h4 class="alert-heading"><strong>Info</strong></h4>
        <p>This is the body.</p>
        <p>Even multi-line is possible.</p>
        </div>"""
    )

    # when
    actual = md.convert(pattern)

    # then
    assert expected == actual


def test_conversion_overwriting_heading() -> None:
    """Test conversion with additional heading parameter."""
    # given
    md = Markdown(extensions=[AlertExtension()])
    pattern = textwrap.dedent(
        """
        :: info heading="Alternative Heading"
        This is the body.
        ::
        """
    )
    expected = textwrap.dedent("""\
        <div class="alert alert-info" role="alert">
        <h4 class="alert-heading"><strong>Alternative Heading</strong></h4>
        <p>This is the body.</p>
        </div>"""
    )

    # when
    actual = md.convert(pattern)

    # then
    assert expected == actual
