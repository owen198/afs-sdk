
## Usage Steps

# Step1: Create

# Step2: Upload

# Step3: Pack

# Step4: Download

# Call otapackager-cli

### Request

`GET /pack/`

|Status Code           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
|200                   | package successed                                                   |
|211                   | `model.bat` does not exist                                          |
|212                   | `model.pkl` does not exist                                          |

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

    curl -X POST -F file=@model.pkl http://${HOST}/upload

|Status Code           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
|200                   | Upload successed                                                    |
|211                   | flask.request() ValueError, usually give wrong argv                 |
|212                   | flask.request() IOError, please check PATH_MODEL at server site     |
|213                   | File extension does not allowed, only accept `.zip` and `.bat`      |
|500                   | flask.request() execptions                                          |


## CloudFoundry push commend
`cf push owen_otahub_test_u32 --docker-image cfleu198/ubuntu32 -c "python /root/afs-sdk/ota/FileServer.py" -k 2g -m 2g`

## DockerHub Push commend
