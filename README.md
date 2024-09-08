# FastAPI Websockets with Javascript 
This is a simple web socket chat application I built in this [livestream](https://www.youtube.com/live/5o__C9wJHZA?si=L5xwYWZiYGXot-es)

<video width="640" height="360" controls>
  <source src="./assets/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## How to run the app

### Run the app locally
You can install the requirements locally using the following command
```bash
pip install -r requirements.txt
```
Then finally, run the app with the following command
```bash
fastapi dev 
```
### Run the application in Docker
You can run the app using Docker with
```bash
docker build -t <image name>
```

```bash
docker run -p 8000:8000 <image name>
```