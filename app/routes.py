from flask import render_template, current_app as app
import random

quotes = [
    "Ben seni bir ömür sevmeye değil, sana bir ömür olmaya geldim.",
    "Kalbimde taşıdığım en büyük hakikat, sana duyduğum aşktır.",
    "Sana her baktığımda, dünyayı değil; kendi cennetimi görürüm.",
    "Benim için aşk, adını içimde sakladığım en kıymetli sırdır.",
    "Sensiz geçen zaman, varlığınla telafi edilen bir eksiklikten ibarettir."
]


@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)
