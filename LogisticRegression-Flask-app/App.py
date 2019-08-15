from flask import Flask,request,render_template
import joblib

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

def Ad_Click(age,male,time_spent,E_use):
    model = joblib.load('Advertising_model.sav')
    predictions = model.predict([[age,male,time_spent,E_use]])
    return predictions

@app.route("/logistic",methods = ['POST', 'GET'])
def logistic():
    if (request.method == 'POST'):
        values = request.form
        print(values)
        country_name = values['Country']
        age = values['Age']
        male = values['Male']
        time_spent = values['Daily Time Spent on Site']
        E_use = values['Daily Internet Usage']
        time_spent = int(time_spent)
        E_use = int(E_use)
        age = int(age)
        male = int(male)

        click_ad = Ad_Click(age,male,time_spent,E_use)

        data = {
            'country': country_name,
            'age': age,
            'male': male,
            'time_spent': time_spent,
            'E_use': E_use,
            'click_ad': click_ad[0]
        }

        return render_template('Logistic _Regression.html', data = data)




if __name__ == '__main__':
    app.run()
