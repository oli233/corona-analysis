build:
	docker build -t olly233/corona_api:latest -f ./API/Dockerfile .
deploy:
	docker run --name api -dit -p 5000:5000/tcp --restart always olly233/corona_api:latest
clean:
	docker rm -f api
redeploy: clean build deploy

buildf:
	docker build -t olly233/fetch:latest -f ./Fetch_Graphs/Dockerfile .
deployf:
	docker run --name fetch -it -v /opt/figures:/app/figures --rm olly233/fetch:latest
cleanf:
	docker rm -f fetch

buildredis:
	docker build -t olly233/redis:latest -f ./redis/Dockerfile .
redis:
	docker run --name redis -it -d -p 6350:6379 --restart always olly233/redis:latest
redeployr:
	docker rm -f redis
	docker build -t olly233/redis:latest -f ./redis/Dockerfile .
	docker run --name redis -it -d -p 6350:6379 --restart always olly233/redis:latest
