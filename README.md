# API Telemedicina
![](https://img.shields.io/badge/Editor-VisualCode-informational?style=flat&logo=#3776AB&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Language-Python3-informational?style=flat&logo=#3776AB&logoColor=white&color=2bbc8a)

# Hospedado no cloud Heroku(temporariamente)
![](https://img.shields.io/badge/CLOUD-HEROKU-informational?style=flat&logo=#3776AB&logoColor=white&color=2bbc8a)  
https://apidesafiotelemedicina.herokuapp.com/
# WEB API Main Tasks
- /SIGNIN
- /SIGNUP
- /PRODUCT
- /PRODUCT/{id}
- /ORDERS
- /ORDERS/{orderid}
- /ORDERS/search

# INSTALLATION
- Create an envorinment folder "venv"
"python -m venv tele_venv"

- Install dependencies
 "pip install -r requirements.txt"

- Database migration
"python manage.py makemigrations"
"python manage.py migrate"

- Run serve
"python manage runserver"
