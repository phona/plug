build: app-image
	@cd htmls && make

app-image: Dockerfile $(shell find . -name "*.py")
	@echo "Buiding image for app..."
	@docker build --tag=plug-app .
	@date > app-image
