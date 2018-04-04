
## Usage Steps

### Step1: Create

Assuming that `model.pkl` and `model.bat` had been created by AFS Task (Trigger)

### Step2: Upload

1. Use upload API to upload `model.pkl` and `model.bat` to OTA-Packager APP
2. The uploaded file will be installed in `/root/afs-sdk/ota/model/`
3. If pervious version exists in target folder, it will be removed.

### Step3: Pack (Call otapackager-cli)

1. Use pack API to pack `model.pkl` and `model.bat` as `model.zip`
2. otapackager-cli will be executed in CLI model, an output file be generated in `/root/afs-sdk/ota/`
3. The out file has a random name, we rename it as `model.zip` and move it to `/root/afs-sdk/ota/model/`
4. If pervious version exists in target folder, it will be removed.

### Step4: Download

Use download API to download `model.zip`

## Call otapackager-cli

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
