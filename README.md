# tech-innovation-project-backend

### List all libraries installed
`
pip freeze
`
### Install the Project Locally
`
pip install -r requirements.txt
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

### Install the Project
`
pip install -r requirements.txt
`

### Activate virtualenv
`
source venv/bin/activate
`

### Deactivate virtualenv
`
deactivate
`

### Update requirements.txt file with latest installed dependencies
`
pip3 freeze > requirements.txt
`

### Deploy tot heroku after last commit
`
git push heroku main
`
Refer
(Tutorial)[https://devcenter.heroku.com/articles/git#create-a-heroku-remote]
