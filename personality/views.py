from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import requests, json
from requests.auth import HTTPBasicAuth


# represents the index page and renders the index.html page.
# templates folder is registered in our settings file as our templates directory
# which makes it easy for the server to get our index.html page
def index(request):
    reviews = []
    if request.POST:
        reviewerText = request.POST['reviewerText']
        print reviewerText
    else:
        with open(settings.MEDIA_ROOT + "/reviews_amazon_instant_31.json") as review:
            reviews = json.load(review)
    return render(request, "personality/index.html", {'reviews': reviews})


def review(request):
    reviews = []
    with open(settings.MEDIA_ROOT + "/reviews_amazon_instant_31.json") as review:
        reviews = json.load(review)
    if request.POST:
        index = request.POST['index']
        reviewText = reviews[int(index)]["reviewText"]
        reviewerName = reviews[int(index)]["reviewerName"]
        cred = open(settings.MEDIA_ROOT + "/insights_cred.json", 'r')
        credentials = json.load(cred)
        url = credentials["url"] + "/v3/profile"

        querystring = {"version": "2016-10-20"}

        payload = reviewText
        headers = {
            'content-type': "text/plain;charset=utf-8",
        }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring, auth=HTTPBasicAuth(credentials["username"], credentials["password"]))
        formatted_word, json_result = format(response.text)
        formatted_word['reviewText'] = reviewText
        personality, needs, values = format_D3(json_result)
        personality_data = {}
        personality_data["name"] = reviewerName
        personality_data["percentile"] = "NA"
        personality_data["children"] = []
        personality_data["children"].append(personality)
        personality_data["children"].append(needs)
        personality_data["children"].append(values)
        formatted_word['personality_data'] = personality_data
    return JsonResponse(formatted_word)


def format(response):
    result = json.loads(response)
    personality_words = []
    personality = result["personality"]
    for index in personality:
        new_dict = {}
        index_name = index["name"]
        index_children = index["children"]
        index_percentile = index["percentile"]
        new_dict['text'] = index_name
        new_dict['weight'] = index_percentile
        personality_words.append(new_dict)
        for child in index_children:
            new_dict = {}
            index_name = child["name"]
            index_percentile = child["percentile"]
            new_dict['text'] = index_name
            new_dict['weight'] = index_percentile
            personality_words.append(new_dict)

    needs_words = []
    needs = result["needs"]
    for index in needs:
        new_dict = {}
        index_name = index["name"]
        index_percentile = index["percentile"]
        new_dict['text'] = index_name
        new_dict['weight'] = index_percentile
        needs_words.append(new_dict)

    values_words = []
    values = result["values"]
    for index in values:
        new_dict = {}
        index_name = index["name"]
        index_percentile = index["percentile"]
        new_dict['text'] = index_name
        new_dict['weight'] = index_percentile
        values_words.append(new_dict)

    formatted_word = {}
    formatted_word["personality"] = personality_words
    formatted_word["needs"] = needs_words
    formatted_word["values"] = values_words
    return formatted_word, result


def format_D3(personality_data):
    personality = {}
    personality["name"] = "Personality"
    personality["children"] = personality_data["personality"]
    personality["percentile"] = "NA"

    needs = {}
    needs["name"] = "Needs"
    needs["children"] = personality_data["needs"]
    needs["percentile"] = "NA"

    values = {}
    values["name"] = "Values"
    values["children"] = personality_data["values"]
    values["percentile"] = "NA"
    return personality, needs, values
