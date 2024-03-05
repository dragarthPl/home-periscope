.PHONY: run-dev
run-dev:
	poetry run python src/main/home_periscope.py

.PHONY: build-frontend
build-frontend:
	cd frontend && pnpm build && cd ..

.PHONY: build-docker
build-docker:
	docker build -t home-periscope .

.PHONY: run-docker
run-docker:
	docker run -it --rm -p 5000:5000 home-periscope

.PHONY: run-docker-interactive
run-docker-interactive:
	docker run -it --rm -p 5000:5000 --entrypoint /bin/bash home-periscope

,PHONY: run-docker-dev
run-docker-dev:
	docker run -it --rm -p 5000:5000 -v $(shell pwd)/:/app