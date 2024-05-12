from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__,template_folder='template')

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        targeted_productivity = request.form['targeted_productivity']
        svm = request.form['svm']
        wip = request.form['wip']
        over_time = request.form['over_time']
        incentive = request.form['incentive']
        idle_time = request.form['idle_time']
        idle_men = request.form['idle_men']
        no_of_worker = request.form['no_of_workers']
        department = request.form['department']
        day = request.form['day']
        quarter = request.form['quarter']
        
        feature_list = []

        feature_list.append(float(targeted_productivity))
        feature_list.append(float(svm))
        feature_list.append(float(wip))
        feature_list.append(float(over_time))
        feature_list.append(float(incentive))
        feature_list.append(float(idle_time))
        feature_list.append(int(idle_men))
        feature_list.append(int(no_of_worker))
       
        department_list=['0','1']
        day_list = ['0','1','2','3','4','5']
        qaurter_list = ['1','2','3','4']
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        

        traverse_list(department_list, department)
        traverse_list(day_list, day)
        traverse_list(qaurter_list, quarter)
        print(feature_list)
        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],3)
        pred_value
    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)