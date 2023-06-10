"""WORDLP - NLP demonstration"""
from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_lg')

@app.route('/index', methods=['GET', 'POST'])
def analyze_text():
    """Analyze text"""
    if request.method == 'POST':
        text = request.form['text']
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
        return render_template('index.html', text=text, entities=entities, dependencies=dependencies)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


