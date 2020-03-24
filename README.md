## BUILD FROM LOCALLY
export proxy_host=127.0.0.1 && \
export proxy_port=8079 && \
sudo docker build --no-cache -t <image>:<tag> --network=host --build-arg proxy_host="$proxy_host" --build-arg proxy_port="$proxy_port" .
## Running Docker Container Locally
run the container using the host networking
sudo docker run --network=host -e proxy_host="<proxy_host>" -e proxy_port="<proxy_port>" -it <docker_image>

There are a few alternative build docker image using entrypoint.sh or set proxy conf execute setup-proxy.sh

