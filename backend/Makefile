.PHONY: start-local start-prod collect-static create-admin

export PYTHONPATH := src

start-local:
	@echo "🔄 Running migrations..."
	poetry run python -m manage migrate
	@echo "📂 Collecting static files..."
	poetry run python -m manage collectstatic --noinput
	@echo "🚀 Starting server with Uvicorn..."
	poetry run uvicorn server.asgi:app --host 0.0.0.0 --port ${TCP_PORT} --reload

start-prod:
	@echo "🔄 Performing migrations..."
	poetry run python -m manage migrate
	@echo "📂 Collecting static files..."
	poetry run python -m manage collectstatic --noinput
	@echo "🚀 Starting server in production mode..."
	poetry run uvicorn server.asgi:app --port ${TCP_PORT} --host 0.0.0.0

collect-static:
	@echo "🗂️ Collecting static files..."
	poetry run python -m manage collectstatic --noinput

create-admin:
	@echo "🧑‍💻 Creating superuser..."
	poetry run python -m manage createsuperuser
