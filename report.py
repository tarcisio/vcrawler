import json
from jinja2 import Template

template = Template('''
<html>
    <head><title>produtos</title></head>
    <body>
        {% for p in produtos %}
        <div>
            <h1><a href="{{p.url}}">{{p.name}}</a> ({{p.sku}}) - ${{p.price}}</h1>
            <p>{{p.description}}</p>
        </div>
        {% endfor %}
    </body>
</html>
''')

produtos = []

with open("out.jl", "r") as ins:
    for line in ins:
        obj = json.loads(line)
        produtos.append(obj)

print(template.render(produtos=produtos))
