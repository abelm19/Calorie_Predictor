from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_calories_burnt' , methods = ['GET', 'POST'])
def predict_calories_burnt():

   gender = (request.form['gender'])
   age = int(request.form['age'])
   height = float(request.form['height'])
   weight = float(request.form['weight'])
   duration = float(request.form['duration'])
   heart_rate = float(request.form['heart_rate'])
   body_temp = float(request.form['body_temp'])

   response = jsonify({
        'estimated_calories_burnt': util.get_estimated_calories(gender, age, height, weight, duration, heart_rate,
                                                                body_temp)
    })
   response.headers.add('Access-Control-Allow-Origin', '*')

   return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Calories Burnt Prediction...")
    util.load_saved_artifacts()
    app.run()
