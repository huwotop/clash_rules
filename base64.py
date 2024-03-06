import base64

with open('jiedian.txt', 'r', encoding='utf-8') as f:
    with open('jiedian.md', 'w') as f2:
        str = f.read()
        f2.write(base64.b64encode(str.encode('utf-8')).decode('utf-8'))
