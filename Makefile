.PHONY: help build clean deploy

help:
	@echo "nwb4edu Jupyter Book - Make commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make build   - Build the Jupyter Book"
	@echo "  make clean   - Clean the build directory"
	@echo "  make deploy  - Build and deploy to GitHub Pages"
	@echo "  make help    - Show this help message"

build:
	@echo "Building Jupyter Book..."
	jupyter-book build .

clean:
	@echo "Cleaning build directory..."
	jupyter-book clean .
	@echo "Build directory cleaned."

deploy: clean build
	@echo "Deploying to GitHub Pages..."
	ghp-import -n -p -f _build/html
	@echo "Deployed successfully!"
