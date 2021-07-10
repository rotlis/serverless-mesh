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

login:
	saml2aws login

create_ns:
	@echo ****Creating namespace ${name}
	aws servicediscovery create-http-namespace --name ${name}

create_service:
	@echo ****Creating service ${name} in ns ${ns}
	aws servicediscovery create-service --name ${name} --namespace-id ${ns}

create_instance:
	aws servicediscovery register-instance --service-id ${service_is} --instance-id ${instance_id} --attributes ${attrs}


# 	saml2aws login -a $(2) -r $(3) && \

define show_usage
	printf "Usage:\n"
	printf "${YELLOW}make login            ${GREEN}Saml login${NC}\n"
	printf "${YELLOW}make create_ns        ${GREEN}Create namespace${NC}\n"
	printf "${YELLOW}make create_service   ${GREEN}Create service${NC}\n"
	printf "${YELLOW}make create_instance  ${GREEN}Create instance${NC}\n"
	printf "${NC}\n"

endef
