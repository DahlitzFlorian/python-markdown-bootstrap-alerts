# Boostrap alerts extension for Python-Markdown

![Tests](https://github.com/DahlitzFlorian/python-markdown-bootstrap-alerts/actions/workflows/main.yml/badge.svg?branch=master)

This extension adds bootstrap alerts support to [Python-Markdown].

[Python-Markdown]: https://github.com/Python-Markdown/markdown


## Installation

### Install from PyPI

```
$ python -m pip install mdx_alerts
```

### Install locally using poetry

Use `poetry build` to build the extensions.
Then, you can install it via pip:

```shell
$ python -m pip install dist/mdx_alerts-1.0.0-py3-none-any.whl
```


## Usage

There are two different ways to use the extensions.
Either, by using its identifier `mdx_alerts`:

```python
>>> import markdown
>>> md = markdown.Markdown(extensions=["mdx_alerts"])
```

... or by supplying an instance of `AlertExtension`:

```python
>>> import markdown
>>> from mdx_alerts import AlertExtension
>>> md = markdown.Markdown(extensions=[AlertExtension()])
```


## Markdown pattern and customization

The pattern starts with two colons follows by the alert level, e.g. info.
Everything after the newline character is counted towards the alert message/body until on an empty line the two colons appear again.

```markdown
:: info
This is the body.

Even multi-line is possible.
::
```

The above snippet results in:

```html
<div class="alert alert-info" role="alert">
    <h4 class="alert-heading"><strong>Info</strong></h4>
    <p>This is the body.</p>
    <p>Even multi-line is possible.</p>
</div>
```

Additionally, you can overwrite the default heading by supplying an alternative via the `heading=` attribute after the alert level:

```markdown
:: info heading="Alternative Heading"
This is the body.
::
```

... which results in:

```html
<div class="alert alert-info" role="alert">
    <h4 class="alert-heading"><strong>Alternative Heading</strong></h4>
    <p>This is the body.</p>
</div>
```
