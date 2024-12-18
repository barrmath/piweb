#!/bin/bash
git checkout test ;
git pull ;
python -m venv venv ;
source venv/bin/activate ;
pip install -r requirements.txt ;
sass web_app/static/scss/main.scss web_app/static/css/main.css;
pytest ;
test=echo$? ;
if ((test == 0));then
    git checkout main;
    git merge test;
    git push origin main;
    exit 0;     
else
    exit 1;
fi