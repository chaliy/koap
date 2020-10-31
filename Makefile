build:
	cd ./koap-ui && npm install && npm run build
	cd ./koap && pipenv install

test:
	cd ./koap-ui && npm install && CI=true npm test

local-run:
	cd ./koap && make local-run

# Docker image

IMAGE_TAG?=latest
IMAGE_NAME ?= ghcr.io/chaliy/koap:$(IMAGE_TAG)

docker-image-build:
	@ docker build . --tag ${IMAGE_NAME}

docker-image-publish:
	@ docker push ${IMAGE_NAME}

docker-image-run:
	@ docker run -it -p 8080:8080 ${IMAGE_NAME}


# Kubernetes
NS?=koap-dev

ns:
	@ kubectl get namespace $(NS) || (\
		echo "[ns][kubectl]: create namespace $(NS)"; \
		kubectl create namespace $(NS) \
	)
	@ kubectl config set-context --current --namespace=$(NS)