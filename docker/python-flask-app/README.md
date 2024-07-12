# Goal
Create a flask app, build and push image to Github Container Registry/Docker Hub. 

```
# Terminal One
# Build docker image
docker build -t flask-docker-img:latest .

# Run docker image, expose port 5000
docker run -p 5000:5000 flask-docker-img:latest

# In another terminal window
 ~  » curl localhost:5000/
Running Flask!%

# Login to docker
docker login -u <username>

# Push built image
docker push <username>/flask-docker-img:latest
```

---

# Other Useful Docker Commands

### For Images
| Description | Command |
| ------ | ------ |
| Build an image from Dockerfile with a tag | docker build -t <image_name>:<tag>. |
| List images | docker images |
| Delete image | docker rmi <image_name> |
| Remove all unused images | docker image prune |

