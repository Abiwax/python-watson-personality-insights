# python-watson-personality-insights
Python Personality Insights with IBM Bluemix Python SDK
 
This is a simple application that makes use of the IBM Watson Personality Insight service to graphical display traits of users that made reviews on some amazon instant videos.
It makes use of JQCloud javascript library and d3.js library to graphical show the data.

## Install and setup the prerequisites below:

* [Bluemix account](https://console.ng.bluemix.net/registration/)
* [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [Django](https://www.djangoproject.com/download/)

## To begin running locally:
1. Get your personality insight credentials from IBM Bluemix and input the credentials in media/insights_cred.json
2. On your terminal, run ```python manage.py migrate``` and ```python manage.py runserver``` to run the application locally.
3. Run ```http://127.0.0.1:8000/``` on your browser to view the application.

## To begin running on bluemix:
The manifest.yml includes basic information about your app, such as the name, how much memory to allocate for each instance and the route., change the current settings to your application name
The run.sh file contains the commands required to start the server.

1. Choose your API endpoint from the list below
   ```cf api <API-endpoint>```
  
|URL                             |Region          |
|:-------------------------------|:---------------|
| https://api.ng.bluemix.net     | US South       |
| https://api.eu-gb.bluemix.net  | United Kingdom |
| https://api.au-syd.bluemix.net | Sydney         |

2. Login to your Bluemix account

  ```
cf login
  ```

3. Push your application to Bluemix.
  ```
cf push
  ```

4. Get the url listed in the output of the push command, go to abipersonality/settings and add that url to your list of allowed hosts on line 28.

5. Run ```cf push``` again.

6. Open the url listed in the output of the push command e.g(*url.mybluemix.net*) on a browser to view your app.

7. Make any changes you want and re-deploy to Bluemix using ```cf push```

8. To Deploy this on IBM Bluemix, use the button below.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy/repository=https://github.com/Abiwax/python-watson-personality-insights.git)

  #### ScreenShots
<div>
<img src="/media/shot.png?raw=true" height="400" alt="WordCloud">
</div>
