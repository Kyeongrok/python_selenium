### Godpia사용법

GODPIA_ID, GODPIA_PASSWORD를 environment variable로 넣고 사용 하세요.

mode는 debug모드와 login모드가 있습니다.

### Docker로 실행

```
docker build godpia_writer . 
docker run --env GODPIA_ID=<id> --env GODPIA_PASSWORD=<password> godpia_writer env
```

### Docker build하고 push
image는 Docker hub에 업로드 되어 있습니다.

https://hub.docker.com/repository/docker/oceanfog1/godpia-writer

```
docker build -t oceanfog1/godpia-writer:<tagname> .
docker push oceanfog1/godpia-writer:<tagname>
```

ex) docker run --env GODPIA_ID=oceanfog1 --env GODPIA_PASSWORD=password1 godpia_writer env


### chrome을 debug모드로 열기

시작 -> 실행 후 아래 명령어로 실행 합니다.

```shell
C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
```