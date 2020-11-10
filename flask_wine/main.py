import numpy as np
import pandas as pd
import pickle, joblib
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Import pipeline for ML
with open("models/data_preparation_pipe.pkl", "rb") as f:
	pipe = pickle.load(f)

# Import model for ML prediction
with open("models/svr.jbl", "rb") as g:
	model = joblib.load(g)

# Data in good shape
def good_data(features, list_values):
	df = pd.DataFrame(columns=features)
	df.loc[0] = list_values
	return df

# To Find
def sentence_and_image(nb):
	if nb <= 85:
		return "Do you really like \"piquette\" ?", "BadWine"

	elif nb >= 95:
		return "Wooow !! What a wine !!", "ExcellentWine"

	else:
		return "Seems to be a good wine !", "GoodWine"



@app.route('/', methods=['GET'])
def wine_index():
	return render_template("index.html")



@app.route('/predict/', methods=['POST'])
def result():
	price_val = float(request.form['WinePrice'])
	province_val = str(request.form['WineProvince'])
	variety_val = str(request.form['WineVariety'])
	winery_val = str(request.form['Winery'])
	region_1_val = str(request.form['WineRegion'])

	data_ok = good_data(features=['price', 'province', 'variety', 'winery', 'region_1'],
						list_values=[price_val, province_val, variety_val, winery_val, region_1_val])

	data_transformed = pipe.transform(data_ok)

	pred = int(model.predict(data_transformed)[0])

	return render_template("prediction.html", notation=pred, wine_type=sentence_and_image(pred)[1], sentence=sentence_and_image(pred)[0])




if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
