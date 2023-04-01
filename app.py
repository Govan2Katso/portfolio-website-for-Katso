from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
    'id':1,
    'title':'Web Developer',
    'location':'Kuruman'

    },
    {
    'id':2,
    'title':'Penetration Tester',
    'location':'Remote'
    },
    {
    'id':3,
    'title':'Software Developer',
    'location':'Kathu'
    },
    {
    'id':4,
    'title':'Security Analyst',
    'location':'Cape Town' 
    }


]

@app.route('/')
def job_opennings():
    return render_template('home.html', jobs=JOBS, company_name='Katso')




if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug=True)