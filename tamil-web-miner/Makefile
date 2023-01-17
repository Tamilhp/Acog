.DEFAULT_GOAL := help
.PHONY: help api-docs
.SILENT: api-docs

# dockerbuild dir (cpu/gpu)
DOCKERBUILD_FOLDER=gpu

# run environment (dev:0 / server: 1)
RUN_ENV=1

help: ## This prints help text for all the existing commands
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%25s:\033[0m %s\n", $$1, $$2}'

clean: ## Cleans the folders
	rm -rf *.egg-info
	find . -name ".DS_Store"  -exec rm -rf {} +
	find . -name "__pycache__" -exec rm -rf {} +

docs:  ## Makes documentation from all the subsystems
	cd docs; make docs

publish: ## Publishes the docuemntation
	cd docs; make publish

modules-dev: ## Installs the modules for dev purposes
	cd modules; make install-dev

modules: ## Installs the modules for prod
	cd modules; make install-prod

install-models: ## Installs the models for the project at ATK_PROJECTS_FOLDER
	cd models; make install-prod

init: modules-dev install-models	## Developer intialization

init-prod: modules install-models ## Production ready installation for root

test: init ## Runs the tests
	cd apps; make test

package-for-test: ## Makes a package for testing
	echo "To be done"

package-for-prod: ## Makes a production ready package.
	echo "To be done"

sanity-test: ## Tests the project folder to see if complies to the layouts
	echo "To be done"

sphinx-setup:
		(rm -rf ref_docs/source/*.rst)
		(pandoc --from=markdown --to=rst --output=ref_docs/source/readme.rst README.md)
		(cat ref_docs/source/readme.rst ref_docs/source/index.rst.tmpl > temp && mv temp ref_docs/source/index.rst)
		(rm -rf ref_docs/source/readme.rst)

api-docs: sphinx-setup ## Generate Sphinx API docs
		(cd ref_docs && ./build_start.sh && ${MAKE} html)

run-trainers: ## Run trainers of all models
	cd models && make run-trainers

publish-api-docs: api-docs ## Publish generated Sphinx documentation
	cd ref_docs/build/html; python -m http.server

pip-freeze: ## Freeze python requirements

		pip freeze | cat requirements.txt - | sort | uniq > all_reqs.txt

		sed -i '' '/^#/d' all_reqs.txt
		sed -i '' '/^-e/d' all_reqs.txt

		cp all_reqs.txt requirements.txt
		cp all_reqs.txt dockerbuild/cpu/python_requirements.txt
		cp all_reqs.txt dockerbuild/gpu/python_requirements.txt

		# Replace tensorflow with tensorflow-gpu if found
		sed -i -e 's/tensorflow/tensorflow-gpu/g' dockerbuild/gpu/python_requirements.txt

		@grep -q 'tensorflow' requirements.txt 2>/dev/null || true

		# Removing tensorflow from outer requirements.txt since, we cannot rely on pip-freeze from dev-box to tell
		# which cpu/gpu version of tensorflow is needed.
		sed -i '' '/^tensorflow/d' requirements.txt 2>/dev/null || true

		# Clean up
		rm all_reqs.txt dockerbuild/gpu/python_requirements.txt-e

		@echo "Removing tensorflow in requirements.txt. If you need tensorflow, manually install it."

create_dockerfile: dockerbuild/dockerfile_config.yaml ## Create Dockerfile, build_image.sh using template
		atk-docker.sh dockerfile dockerbuild/dockerfile_config.yaml dockerbuild/$(DOCKERBUILD_FOLDER)

create_container_runner: dockerbuild/run_container_config.yaml ## Create run_container.sh using template
		atk-docker.sh container dockerbuild/run_container_config.yaml dockerbuild/$(DOCKERBUILD_FOLDER) $(RUN_ENV)

build_image: dockerbuild/$(DOCKERBUILD_FOLDER)/Dockerfile dockerbuild/$(DOCKERBUILD_FOLDER)/build_image.sh ## Run generated build_image.sh
		atk-docker.sh build_image dockerbuild/$(DOCKERBUILD_FOLDER)

run_container: dockerbuild/$(DOCKERBUILD_FOLDER)/run_container.sh ## Run generated run_container.sh
		atk-docker.sh run_container dockerbuild/$(DOCKERBUILD_FOLDER)

create_docker_env: create_dockerfile create_container_runner ## Create Dockerfile,build_image.sh and run_container.sh
