build:
	cd ./koap-ui && npm install && npm run build
	cd ./koap && pipenv install

test:
	cd ./koap-ui && npm install && CI=true npm test

local-run:
	cd ./koap && make local-run


IMAGE_TAG?=latest
IMAGE_NAME ?= ghcr.io/chaliy/koap:$(IMAGE_TAG)

docker-image-build:
	@ docker build . --tag ${IMAGE_NAME}

docker-image-publish:
	@ docker push ${IMAGE_NAME}

docker-image-run:
	@ docker run -it -p 8080:8080 ${IMAGE_NAME}
