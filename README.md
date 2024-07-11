# DockerTest
To test:
- Networking/Ports
- Internet/VPN access
- Base images

docker image build -t flask_docker .
docker run -p 5000:5000 -d flask_docker

docker build -t gradio-app .
docker run -p 7860:7860 gradio-app

# Gradio
https://www.gradio.app/guides/deploying-gradio-with-docker
http://localhost:7860/

# Flask
https://blog.logrocket.com/build-deploy-flask-app-using-docker/
https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
http://localhost:5000/
http://172.17.0.2:5000/

# Docker
https://docs.docker.com/network/