build:
	#@docker-compose run build
	docker build -t geo-parser_build .
	
env: 
	@docker-compose run env

ls: 
	@docker-compose run ls

python: 
	@docker-compose run python

shell: 
	@docker-compose run shell

run: 
	@docker-compose run run