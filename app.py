import os
from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

def get_py_files():
    return [f for f in os.listdir('.') if f.startswith('v') and f.endswith('.py')]

def get_description(filename):
    with open(filename, 'r', encoding='utf8') as f:
        first_line = f.readline()
        if first_line.startswith('"""') or first_line.startswith('#'):
            return first_line.strip('"\n# ')
        return 'No description available.'

@app.route('/')
def index():
    files = get_py_files()
    script_data = [{
        "name": f,
        "desc": get_description(f)
    } for f in files]
    template = """
    <h1>Versioned Python Turtle Scripts (v1-v12)</h1>
    <ul>
    {% for script in script_data %}
      <li>
        <strong>{{ script.name }}</strong>: {{ script.desc or 'No description.' }}
        [<a href="/download/{{ script.name }}">Download</a>]
      </li>
    {% endfor %}
    </ul>
    """
    return render_template_string(template, script_data=script_data)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('.', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
