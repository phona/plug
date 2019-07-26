run: build
	@echo "Run docker..."
	@docker-compose up -d
	@docker-compose exec plug-app sh cmd.sh init

build: app-image
	@cd htmls && make

app-image: Dockerfile $(shell find . -name "*.py")
	@echo "Buiding image for app..."
	@docker build --tag=plug-app .
	@date > app-image
