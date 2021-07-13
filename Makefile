#################################################################################
# DOCKER                                                                        #
#################################################################################

run:
	docker-compose up
shell:
	docker-compose run --rm timbre-model bash
install-nvidia-toolkit:
	bash install_nvidia_container_toolkit.sh $(echo $distribution)
build-image:
	bash build.sh
