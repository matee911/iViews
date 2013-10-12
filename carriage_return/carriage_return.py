# coding: utf-8

if __name__ == '__main__':
    print """>>> '<lorem ipsum dolor sit amet%s>' % 'abc\\r\\n'.replace('\\n', '<br />')"""
    print '<lorem ipsum dolor sit amet%s>' % 'abc\r\n'.replace('\n', '<br />')
    print 'Q: What happend with that string?'
