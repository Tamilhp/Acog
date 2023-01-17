.DEFAULT_GOAL := help
.PHONY: help

help: ## This prints help text for all the existing commands
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%25s:\033[0m %s\n", $$1, $$2}'

install: poetrycmd prereqs ## Installs the prerequisites

poetrycmd: ## Installs poetry command
	@echo Installing poetry
	pip install poetry

prereqs: ## installs the prereqs using poetry
	@echo installing prereqs using poetry
	poetry install

clean: ## Cleans pycache
	@echo cleaning the app
	rm -rf */__pycache__

run: ## Runs the app. Go to port 8000 to test it.
	@echo running the app
	poetry run fastapiserver
