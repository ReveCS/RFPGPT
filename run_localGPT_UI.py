from flask import Flask, render_template, request
from flask import Flask, redirect, url_for, request
from run_localGPT import extract_headers, match_and_extract
from ingest import load_documents
from constants import SOURCE_DIRECTORY

app = Flask(__name__)

@app.route('/success/<name>')
def success(doc):
    sections = extract_headers(doc)
    section_strings = []
    for sec in sections:
        string = sec[0] + '  ' + sec[1]
        section_strings.append(string)
    
    l, r = 0, 1

    while r < len(section_strings)/2:
        match_and_extract(doc, section_strings[l], section_strings[r])
        l += 1
        r += 1
    


    return json_object

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        documents = load_documents(SOURCE_DIRECTORY)
        user = request.args.get('nm')
        return redirect(url_for('success',doc = documents[0]))

if __name__ == '__main__':
   app.run(debug = True)