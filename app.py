from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def word_as_image():
    if request.method== 'GET':
        return render_template('home.html')
    else:
        semantic_concept = request.form.get('semantic_concept')
        print(semantic_concept)
        optimized_letter= request.form.get('optimized_letter')
        print(optimized_letter)
        font= request.form.get('font')
        seed= int(request.form.get('seed'))   
        os.system(f'python code/main.py --semantic_concept {semantic_concept} --optimized_letter {optimized_letter} --font {font} --seed {seed}')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)