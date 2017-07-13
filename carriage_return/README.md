Question: What happend with that string?

```python
>>> print '<lorem ipsum dolor sit amet%s>' % 'abc\r\n'.replace('\n', '<br />')
<br />>ipsum dolor sit ametabc
```
