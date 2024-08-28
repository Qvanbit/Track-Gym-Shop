DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
DB_FILE = docker_compose/storages.yaml
DB_CONTAINER = postgres-db
TELEGRAM_FILE = docker_compose/telegram-bot.yaml
TELEGRAM_CONTAINER = telegram-bot
PGADMIN_FILE = docker_compose/pgadmin.yaml
PGADMIN_CONTAINER = pgadmin
DOCKER_STOP = sudo docker stop
REDIS_FILE = docker_compose/redis.yaml
REDIS_CONTAINER = redis

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} -f ${TELEGRAM_FILE} ${ENV} -f ${DB_FILE} ${ENV} -f ${PGADMIN_FILE} ${ENV} -f ${REDIS_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${DB_FILE} -f ${TELEGRAM_FILE} -f ${REDIS_FILE} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: telegram-logs
telegram-logs:
	${LOGS} ${TELEGRAM_CONTAINER} -f

.PHONY: db-logs
db-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER}  bash

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest

.PHONY: pgadmin-stop
pgadmin-stop:
	${DOCKER_STOP} ${PGADMIN_CONTAINER}

.PHONY: redis-logs
redis-logs:
	${LOGS} ${REDIS_CONTAINER} -f
