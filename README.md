# tech-innovation-project-backend

### List all libraries installed

`
pip freeze
`
### Install the Project Locally

Run
`
pip install -r requirements.txt
`
and install all necessary dependencies with below command
`
pip install <package_name>
`

### Create Virtual Environment

`
python3 -m venv <virtual_env_name>
`
### Initial setup before running the applicattion for the first time
#### (This is an optional step and might not be needed)

`export FLASK_APP=src`

### Run Server in debug mode with hot reload
`
python3 main.py
`
### App Runs by default on port 5001
http://127.0.0.1:5001/

Use Virtual env for isolated and consistent development


### Activate virtualenv
`
source <virtual_env_name>/bin/activate
`

### Deactivate virtualenv
`
deactivate
`

### Update requirements.txt file with latest installed dependencies
`
pip3 freeze > requirements.txt
`

### Deploy to heroku after last commit
`
git push heroku main
`

Refer
(Tutorial 1)[https://devcenter.heroku.com/articles/git#create-a-heroku-remote]
(Tutorial 2)[https://devcenter.heroku.com/articles/getting-started-with-python#create-and-deploy-the-app]


### Check if one instance of the app is running
`
heroku ps:scale web=1
`

### Visit the app at the URL shown in the deploy output
`
heroku open
`

### Check heroku logs
`
heroku logs
`