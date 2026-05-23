from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

languages = {
    'en': 'English',
    'hi': 'Hindi',
    'te': 'Telugu',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German'
}

@app.route('/', methods=['GET', 'POST'])
def home():

    translated_text = ""

    if request.method == 'POST':

        text = request.form['text']

        src = request.form['source_language']

        dest = request.form['target_language']

        result = translator.translate(
            text,
            src=src,
            dest=dest
        )

        translated_text = result.text

    return render_template(
        'index.html',
        languages=languages,
        translated_text=translated_text
    )

if __name__ == '__main__':
    app.run(debug=True)
    