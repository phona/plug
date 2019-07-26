all: node_modules/ dist/

node_modules/: package.json
	@echo "Installing..."
	@npm install

dist/: $(shell find src/ -type f) node_modules/
	@echo "Building app..."
	@npm run build
