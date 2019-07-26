build: app-image
	cd htmls && make

app-image: Dockfile $(shell find . -name "*.py")
	@docker build --tag=plug-app .
	@date > app-image
