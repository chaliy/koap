build:
	cd ./koap-ui && npm install && npm run build
	cd ./koap && pipenv install

test:
	cd ./koap-ui && npm install && CI=true npm test
	cd ./koap && pipenv install && make test

local-run:
	cd ./koap && make local-run

# Docker image

IMAGE_TAG?=latest
IMAGE_NAME ?= ghcr.io/chaliy/koap:$(IMAGE_TAG)

docker:
	@ docker build . --tag ${IMAGE_NAME}

docker-image-publish:
	@ docker push ${IMAGE_NAME}

docker-run:
	@ docker run -it -p 8080:8080 ${IMAGE_NAME}


# Kubernetes
NS?=koap-dev

ns:
	@ kubectl get namespace $(NS) || (\
		echo "[ns][kubectl]: create namespace $(NS)"; \
		kubectl create namespace $(NS) \
	)
	@ kubectl config set-context --current --namespace=$(NS)