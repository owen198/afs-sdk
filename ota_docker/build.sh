
docker build -no-cache -t="cfleu198/ubuntu32" .
#docker build -t="cfleu198/ubuntu32" .
docker push cfleu198/ubuntu32
#cf push owen_otahub_test_u32 --docker-image cfleu198/ubuntu32 -c "python /afs-sdk/ota/FileServer.py" -k 2g -m 2g
