DATE = $(shell date +"%Y-%m-%d")

.PHONY: help
help: ## Show help messages
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: # clean
	rm -r .pytest_cache || true
	rm -r .mypy_cache || true
	rm .coverage 2>/dev/null || true
	find . -d -name '__pycache__' | xargs rm -r

.PHONY: typecheck
typecheck: # typecheck
	mypy .

.PHONY: test
test: # test
	poetry run pytest --cov
