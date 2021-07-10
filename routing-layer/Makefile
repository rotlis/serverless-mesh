SHELL  := /bin/bash
RED    := \033[0;31m
GREEN  := \033[0;32m
CYAN   := \033[0;36m
YELLOW := \033[1;33m
NC     := \033[0m # No Color

BUILD_TIME:=`date +%s`

VENV_PATH := ${CURDIR}/venv/bin


usage:
	@$(call show_usage)


clean:
	rm -rf bin && rm -rf temp
	mkdir -p bin
	mkdir -p temp


venv:
	test -d venv || python3 -m venv venv


reset: clean
	rm -rf venv


temp:
	mkdir -p temp


dependencies: venv requirements.txt
	source ${VENV_PATH}/activate; \
	pip install -r requirements.txt --trusted-host apro.nbnco.net.au; \
	deactivate


build: clean venv dependencies

	source ${VENV_PATH}/activate; \
	deactivate

	chmod -R 755 ./bin


coverage: dependencies
	export PYTHONPATH=.; \
	${VENV_PATH}/pytest --cov=. ./test --cov-report=xml --cov-report html:htmlcov

pylintscan: dependencies
	export PYTHONPATH=.; \
	${VENV_PATH}/pylint *.py ${CURDIR}/src --msg-template='{msg_id}: {path}: {line:3d},{column}: {obj}: {msg}'

unit_test: dependencies	
	export PYTHONPATH=.; \
	${VENV_PATH}/pytest ./test --junitxml=./pytest-junit.xml



define deploy
	@echo ****Deploying Lambda [$(3)]

endef

define show_usage
	printf "Usage:\n"
	printf "${YELLOW}make build 			${GREEN}Package your lambda${NC}\n"
	printf "${NC}\n"

endef
