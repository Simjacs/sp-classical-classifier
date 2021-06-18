#################################################################################
# DOCKER                                                                        #
#################################################################################

run:
	docker-compose up
shell:
	docker-compose run --rm timbre-model bash
build-image:
	bash build.sh
