


## Call otapackager-cli

### Request

`GET /pack/`

## Download package

### Request

`GET /download/`

|Status Code           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
|200                   | Package exists and can be downloaded                                |
|211                   | Package does not exists                                             |
|500                   | flask.send_file() execptions                                        |


## Upload pkl or bat files for package 

### Request

`POST /upload/`

    curl -X POST -F file=@model.pkl -F file_path=model http://${HOST}/upload




cf push owen_otahub_test_u32 --docker-image cfleu198/ubuntu32 -c "python /afs-sdk/ota/FileServer.py" -k 2g -m 2g
