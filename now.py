from datetime import datetime

now=datetime.now()
print """Content-Type: text/html
It is <b>%s</b> now.
<img src=/img/time.jpg>"""%(now)