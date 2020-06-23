from flask import Flask, render_template , request, redirect



import joblib
import numpy as np
model = joblib.load("model.pkl")

app = Flask(__name__)

 
@app.route('/')
def hello():
	return render_template("Car-price-html.html")

@app.route('/',methods=['POST'])

def pred():
		one = request.form.get("engine_size",type=float)
		second = request.form.get("curb_weight",type=float)
		third = request.form.get("horse_power",type=float)
		fourth = request.form.get("car_width",type=float)
		fifth = request.form.get("car_length",type=float)
		sixth = request.form.get("wheel_base",type=float)
		seven = request.form.get("bore_ratio",type=float)
		eight = request.form.get("car_height",type=float)
	
		lis = [np.array([one,second,third,fourth,fifth,sixth,seven,eight])]
		my_pred = model.predict(lis)
		my_pred = float(my_pred)
		my_pred = round(my_pred,2)
		return render_template("Car-price-html.html",your_price = my_pred)





if __name__ == '__main__':
	app.run(debug=True)
