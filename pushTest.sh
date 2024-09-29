#!/bin/bash
git push origin dev
git checkout test
git merge dev 
git push origin test
curl --user $USER:$TOKENJENKINS http://0.0.0.0:8090/job/piweb_deploy/buildWithParameters?token=$TOKENJENKINS
git checkout dev