import index.html
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = index.html


@app.route("/")
def index():
    return form


time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name"minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Convert" />
    </form>
    """


@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',
                            minutes='', minutes_error='')


app.run()
