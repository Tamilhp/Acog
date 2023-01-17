.DEFAULT_GOAL := help

help: ## This prints help text for all the existing commands
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%25s:\033[0m %s\n", $$1, $$2}'

api-docs: ## Runs sphinx doc generation for all models
	find . -maxdepth 1 -type d \( ! -name . \) -exec bash -c "cd '{}' && make api-docs" \;

install-prod: ## Installs all sub-dirs as non-editable py packages
	find . -maxdepth 1 -type d \( ! -name . \) -exec bash -c "cd '{}' && make install-prod" \;

install-dev: ## Installs all sub-dirs as editable py packages
	find . -maxdepth 1 -type d \( ! -name . \) -exec bash -c "cd '{}' && make install-dev" \;
