import base64

v = "vmess://ewogICJ2IjogIjIiLAogICJwcyI6ICJKUOiHquW7uuiKgueCuSIsCiAgImFkZCI6ICJkZW1vLmh1d28udG9wIiwKICAicG9ydCI6ICI0NDMiLAogICJpZCI6ICI3MUQwRjI1RS0xMEQ5LTZERDAtM0UwRi04ODUxODFGMjRBREQiLAogICJhaWQiOiAiMCIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6ICJub25lIiwKICAiaG9zdCI6ICIiLAogICJwYXRoIjogIi9odXdvMjA1MHRvcCIsCiAgInRscyI6ICJ0bHMiLAogICJzbmkiOiAiIiwKICAiYWxwbiI6ICIiLAogICJmcCI6ICIiCn0\n"
with open('jiedian.md', 'w') as f:
    with open('jiedian.txt', 'r', encoding='utf-8') as f1:
        str = v + f1.read()        
        f.write(base64.b64encode(str.encode('utf-8')).decode('utf-8'))
