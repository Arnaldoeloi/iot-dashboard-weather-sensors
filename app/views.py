# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from pathlib import Path

import requests
import io
import json
import os
from datetime import datetime

from app import fetch_n_predict



@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def field1(request):

    path = "field_1.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict()
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict()

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)


def field2(request):

    path = "field_2.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/2.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_2_predictions.json",
                                value_column_name = "field2",
                                fetched_file_name = "field_2.json",
                                should_predict = True)
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/2.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_2_predictions.json",
                                value_column_name = "field2",
                                fetched_file_name = "field_2.json",
                                should_predict = True)
        field2(request)

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)

def field1_predict(request):

    path = "field_1_predictions.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/1.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_1_predictions.json",
                                value_column_name = "field1",
                                fetched_file_name = "field_1.json",
                                should_predict = True)
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/1.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_1_predictions.json",
                                value_column_name = "field1",
                                fetched_file_name = "field_1.json",
                                should_predict = True)
        field1(request)

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)

def field2_predict(request):

    path = "field_2_predictions.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/2.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_2_predictions.json",
                                value_column_name = "field2",
                                fetched_file_name = "field_2.json",
                                should_predict = True)
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/2.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_2_predictions.json",
                                value_column_name = "field2",
                                fetched_file_name = "field_2.json",
                                should_predict = True)
        field2(request)

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)

def field3(request):

    path = "field_3.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/3.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_3_predictions.json",
                                value_column_name = "field3",
                                fetched_file_name = "field_3.json",
                                should_predict = False)
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/3.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_3_predictions.json",
                                value_column_name = "field3",
                                fetched_file_name = "field_3.json",
                                should_predict = False)
        field3(request)

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)

def field4(request):

    path = "field_4.json"
    print(os.getcwd())

    if os.path.isfile(path):
        print ("File exists and is readable")
        file = open(path)
        data = json.load(file)
        date_str, sep, tail = data["meta"]["created_at"].partition('.')
        
        last_updated_json_at = datetime.strptime(date_str, '%Y-%d-%m %H:%M:%S')
        now_date = datetime.now()
        
        # Only updates if it has been 5 minutes since last update
        time_diff = now_date - last_updated_json_at
        if(time_diff.seconds > 300):
            fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/4.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_4_predictions.json",
                                value_column_name = "field4",
                                fetched_file_name = "field_4.json",
                                should_predict = True)
            file = open(path)
            data = json.load(file)
            return JsonResponse(data)

        return JsonResponse(data)
    else:
        print ("Either file is missing or is not readable. Creating!")
        fetch_n_predict.fetch_and_predict(csv_fetching_url="https://thingspeak.com/channels/196384/field/4.csv?results=500&api_key=UF678Q0VZLME300M",
                                predictions_file_name = "field_4_predictions.json",
                                value_column_name = "field4",
                                fetched_file_name = "field_4.json",
                                should_predict = True)
        field4(request)

    #response = requests.get("https://thingspeak.com/channels/196384/field/1.json")
    #data = response.json()
    #return JsonResponse(data)





@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
