# !/bin/zsh

docker build -t giich_genshin_image .
docker run -it --name giich_genshin_container --env-file .env giich_genshin_image:latest bash

echo cleaning up...
docker container rm giich_genshin_container
docker image rm giich_genshin_image:latest