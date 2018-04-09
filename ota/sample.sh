#/bin/sh

HOST=owenotahubtestu32.iii-cflab.com

touch model.pkl
touch model.bat
touch model-notallowed.pkl
touch model-notallowed.bat

curl -X POST -F file=@model.pkl http://$HOST/upload
curl -X POST -F file=@model.bat http://$HOST/upload
curl -X POST -F file=@model-notallowed.bat http://$HOST/upload
curl -X POST -F file=@model-notallowed.bat http://$HOST/upload

curl http://$HOST/pack

curl http://$HOST/download
curl http://$HOST/download
