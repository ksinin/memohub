up:
	docker-compose up --build

prune:
	docker containers prune

stop:
	docker-compose down

test:
	docker-compose run app ./manage.py test

restart-app:
	docker restart memohub

shell:
	docker-compose run app ./manage.py shell

bash:
	docker exec -it memohub sh

cs:
	docker-compose run app ./manage.py createsuperuser

