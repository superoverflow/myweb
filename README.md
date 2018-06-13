This is a Django project to run a karaoke server at home!
===

Tips
===
To run shell in alpine use /bin/ash
Use apk instead of apt-get for package management

How to run
===
git pull && docker build -t myweb:latest .
docker kill home
docker run --name home --rm -it -d -p 11080:11080 myweb
