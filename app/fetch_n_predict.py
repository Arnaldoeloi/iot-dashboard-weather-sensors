#!/usr/bin/env python
# coding: utf-8

# # Fetching and preparing data from ThingSpeak
# 

# Data from:
# https://thingspeak.com/channels/196384/feed.csv

# In[1]:


import pandas as pd
from fbprophet import Prophet
import json
import time
from datetime import datetime


def fetch_and_predict(
    csv_fetching_url = "https://thingspeak.com/channels/196384/field/1.csv?results=500&api_key=UF678Q0VZLME300M",
    predictions_file_name = "field_1_predictions.json",
    value_column_name = "field1",
    fetched_file_name = "field_1.json",
    should_predict = True
    ):

    data = pd.read_csv(csv_fetching_url)

    data["created_at"] = pd.to_datetime(data["created_at"]).dt.tz_localize(None)
    data[value_column_name] = pd.to_numeric(data[value_column_name])

    data.drop(['entry_id'], axis=1, inplace=True)


    result = data.to_json(orient="records")

    avg = data[value_column_name].mean()
    var = data[value_column_name].var()
    interval_min = str(data['created_at'].min())+" UTC"
    interval_max = str(data['created_at'].max())+" UTC"
    min = data[value_column_name].min()
    max = data[value_column_name].max()

    current_time = str(datetime.now())

    #parsed = json.loads(result)
    w_meta = json.dumps({"meta": {"created_at":current_time, "min":min,"max":max,"avg":avg, "var":var, "interval_min":interval_min, "interval_max":interval_max }, "data":json.loads(result) })
    parsed = json.loads(w_meta)

    with open(fetched_file_name, 'w') as outfile:
        outfile.write(json.dumps(parsed))


    # In[7]:

    if(should_predict):
        data = data.rename(columns={"created_at":"ds", value_column_name:"y"})

        m = Prophet(daily_seasonality=True)
        model = m.fit(data)

        future = m.make_future_dataframe(periods=100, freq="5min")
        forecast = m.predict(future)
        forecast.tail(5)

        forecast_sensor_df = forecast[['ds','yhat']]
        forecast_sensor_df = forecast_sensor_df.rename(columns={"ds":"created_at", "y":value_column_name})
        forecast_sensor_df = forecast_sensor_df.iloc[-100:]

        avg = forecast_sensor_df["yhat"].mean()
        var = forecast_sensor_df["yhat"].var()
        min = forecast_sensor_df["yhat"].min()
        max = forecast_sensor_df["yhat"].max()
        interval_min = str(forecast_sensor_df['created_at'].min())+" UTC"
        interval_max = str(forecast_sensor_df['created_at'].max())+" UTC"

        result = forecast_sensor_df.to_json(orient="records")
        w_meta = json.dumps({"meta": {"created_at":current_time, "min":min,"max":max, "avg":avg, "var":var, "interval_min":interval_min, "interval_max":interval_max }, "data":json.loads(result) })
        parsed = json.loads(w_meta)

        with open(predictions_file_name, 'w') as outfile:
            outfile.write(json.dumps(parsed))


