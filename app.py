from flask import Flask,render_template,jsonify
JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru India',
        'salary':'Rs 10,00,000'


    },
        {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi India',
        'salary':'Rs 15,00,000'


    },
    {
        'id':3,
        'title':'Frontend Engineer',
         'location':'Remote',
         'salary':'12,00,000'

    },
     {
        'id':4,
        'title':'Backend Engineer',
         'location':'San francico ,Usa',
         'salary':'12,00,000'


    }

]
app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html',jobs=JOBS,company_name='Jovian')

@app.route("/jobs")
def json_func():
    return jsonify(JOBS)
app.run( host='0.0.0.0',debug=True)

   