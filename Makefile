build:
	cd ./koap-ui && npm install && npm run build
	cd ./koap && pipenv install

test:
	cd ./koap-ui && npm install && CI=true npm test

local-run:
	cd ./koap && make local-run