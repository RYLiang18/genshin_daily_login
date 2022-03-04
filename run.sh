# !/bin/zsh

docker build -t giich_genshin_image .
docker run --name giich_genshin_container --env-file .env giich_genshin_image:latest