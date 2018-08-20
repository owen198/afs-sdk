#/bin/sh

echo "200, 200, 213, 213, 200, 211"

#HOST=owenotahubtestu32.iii-arfa.com
#HOST=owenota.wise-paas.com
HOST=otaapi.iii-arfa.com

cp FileServer.py model.pkl
cp FileServer.py model.bat
cp FileServer.py model-notallowed.pkl
cp FileServer.py model-notallowed.bat

curl -X POST -F file=@model.pkl http://$HOST/upload
curl -X POST -F file=@model.bat http://$HOST/upload
curl -X POST -F file=@model-notallowed.bat http://$HOST/upload
curl -X POST -F file=@model-notallowed.bat http://$HOST/upload

curl http://$HOST/pack

curl http://$HOST/download
curl http://$HOST/download

rm -rf ./*.pkl
rm -rf ./*.bat
