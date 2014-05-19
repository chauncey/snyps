#!/usr/bin/env python

"""Snippets app as a Flask app"""

from flask import Flask, render_template
import snippets

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    pagevars = {'content': snippets.get_content(),
                'groups': snippets.get_groups()}
    return render_template('snippets_mobile.html', pagevars=pagevars)


@app.route('/create')
def create():
    return render_template('snippets_mobile_create.html',
                           pagevars={'groups': snippets.get_groups()})


if "__main__" == __name__:
    app.run(host='0.0.0.0', port=80)
    #app.run(debug=True, host='0.0.0.0', port=5001)


