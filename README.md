# tredge

This is tiny yet fast module to get set of explicitly defined transitive edges from an acyclic directed graph. It takes graph represented as dictionary (keys are children, values are iterables with parents), or as iterable of iterables representing edges `((child, parent))`, or file object pointing to tab-delimited file with 2 columns `(child, parent)`, and outputs set of transitive edges found there.

Usage:

```python
import tredge

g = {
    'b': set(['a']),
    'c': set(['a']),
    'd': set(['b', 'c', 'a']),
    'e': set(['d', 'a'])
}
result = tredge.transitive_edges(g)
print(result)

# {('d', 'a'), ('e', 'a')}
```

or

```python
import tredge

g = [
    ('b', 'a'),
    ('c', 'a'),
    ('d', 'b'),
    ('d', 'c'),
    ('e', 'd'),
    ('e', 'a'),
    ('d', 'a')
]
result = tredge.transitive_edges(g)
print(result)

# {('d', 'a'), ('e', 'a')}
```

or

```python
"""input_file.tab:
b	a
c	a
d	b
d	c
e	d
e	a
d	a
"""

import tredge

with open('input_file.tab', mode='r', encoding='utf8') as g:
    result = tredge.transitive_edges(g)
print(result)

# {('d', 'a'), ('e', 'a')}
```
