# Flask app practice: Watch List 

Tutorial: https://tutorial.helloflask.com/

Ch.3

jinja2 usage :

- {{ ... }} to assign variables
- {% ... %} to use condition expression or loop
- {# ... #} to comment。

Ch.5

- How to add custom flask command : https://dormousehole.readthedocs.io/en/latest/cli.html#id9

```python
import click
from flask import Flask

app = Flask(__name__)

@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    ...
```
```commandline
 flask create-user admin
```

- Using GUI to connet to your local db
  - GUI : https://dbeaver.io/download/
  1. Click on the "Database" menu at the top or use the shortcut Ctrl+N (Windows/Linux) or Cmd+N (macOS) to create a new database connection.
  2. In the "Select a driver and data source" window, you can search for "SQLite" or navigate to "SQLite" and select it.
  3. Browse & open your data.db (create by flask initdb)


Ch.6

- @app.context_processor: To inject new variables automatically into the context of a template 
https://flask.palletsprojects.com/en/2.3.x/templating/#context-processors

- If u want to keep the content in parent, add {{ super() }} to do this.
```html
{% block title %}
  {{ super() }}
  <br>
  Wish u have a good time watching movies
{% endblock %}
```