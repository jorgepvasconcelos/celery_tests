CELERY_BIN_PATH = celery
APP_PATH = app
CELERY_ARGS = -A $(APP_PATH) worker --loglevel=INFO

run_celery:
	$(CELERY_BIN_PATH) $(CELERY_ARGS)

container:
	docker-compose up

#run: container run_celery
