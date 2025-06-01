from flask import render_template, current_app as app
import random

quotes = [
    "Seninle bir ömre değil, sonsuzluğa göz kırpıyorum.",
    "Kalbim, senin adını her atışında bir dua gibi fısıldıyor.",
    "Aşk, zamanın ötesinde iki ruhun birbirine yazılmış kaderidir.",
    "Sensizlik, kelimelerin kifayetsiz kaldığı en uzun cümlemdir.",
    "Gözlerin, karanlık gecelerde bile yolumu aydınlatan tek yıldızdır."
]


@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)