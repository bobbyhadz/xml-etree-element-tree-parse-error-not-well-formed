# ParseError: not well-formed (invalid token)

from lxml import etree

data = """
<body>
  <p>bobbyhadz.com \x08</p>
</body>"""

parser = etree.XMLParser(recover=True)

root = etree.fromstring(data, parser=parser)

print(root.tag)  # 👉️ body

# b'<body>\n  <p>bobbyhadz.com </p>\n</body>'
print(etree.tostring(root))

print(root.find('p').tag)  # 👉️ p
