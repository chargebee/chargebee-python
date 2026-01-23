.PHONY: update-version increment-major increment-minor increment-patch test build clean install lint format check publish

# Version file location
VERSION_FILE := VERSION
VERSION_PY_FILE := chargebee/version.py
SETUP_PY_FILE := setup.py

# Python command (use python3 if needed)
PYTHON := python3
PIP := pip3

update-version:
	@echo "$(VERSION)" > $(VERSION_FILE)
	@perl -pi -e 's|VERSION = "[.\-\d\w]+"|VERSION = "$(VERSION)"|' $(VERSION_PY_FILE)
	@if [ -f "$(SETUP_PY_FILE)" ]; then \
		perl -pi -e 's|version="[.\-\d\w]+"|version="$(VERSION)"|' $(SETUP_PY_FILE); \
	fi
	@if [ -f "pyproject.toml" ]; then \
		perl -pi -e 's|^version = "[.\-\d\w]+"|version = "$(VERSION)"|' pyproject.toml; \
	fi
	@echo "Updated version to $(VERSION)"

increment-major:
	$(eval CURRENT := $(shell cat $(VERSION_FILE)))
	$(eval MAJOR := $(shell echo $(CURRENT) | cut -d. -f1))
	$(eval NEW_VERSION := $(shell echo $$(($(MAJOR) + 1)).0.0))
	@$(MAKE) update-version VERSION=$(NEW_VERSION)
	@echo "Version bumped from $(CURRENT) to $(NEW_VERSION)"

increment-minor:
	$(eval CURRENT := $(shell cat $(VERSION_FILE)))
	$(eval MAJOR := $(shell echo $(CURRENT) | cut -d. -f1))
	$(eval MINOR := $(shell echo $(CURRENT) | cut -d. -f2))
	$(eval NEW_VERSION := $(MAJOR).$(shell echo $$(($(MINOR) + 1))).0)
	@$(MAKE) update-version VERSION=$(NEW_VERSION)
	@echo "Version bumped from $(CURRENT) to $(NEW_VERSION)"

increment-patch:
	$(eval CURRENT := $(shell cat $(VERSION_FILE)))
	$(eval MAJOR := $(shell echo $(CURRENT) | cut -d. -f1))
	$(eval MINOR := $(shell echo $(CURRENT) | cut -d. -f2))
	$(eval PATCH := $(shell echo $(CURRENT) | cut -d. -f3))
	$(eval NEW_VERSION := $(MAJOR).$(MINOR).$(shell echo $$(($(PATCH) + 1))))
	@$(MAKE) update-version VERSION=$(NEW_VERSION)
	@echo "Version bumped from $(CURRENT) to $(NEW_VERSION)"

install:
	@echo "Installing package..."
	@$(PIP) install -e .

install-dev:
	@echo "Installing development dependencies..."
	@$(PIP) install -e ".[dev]"
	@$(PIP) install pytest pytest-cov black flake8 pylint mypy

test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest tests/ -v

test-coverage:
	@echo "Running tests with coverage..."
	@$(PYTHON) -m pytest tests/ --cov=chargebee --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

format:
	@echo "Formatting code with ruff.."
	@uvx ruff format .
	
typecheck:
	@echo "Running mypy type checker..."
	@mypy chargebee/ --ignore-missing-imports

check: format-check lint test
	@echo "All checks passed!"

build: clean
	@echo "Building distribution packages..."
	@$(PYTHON) -m build

clean:
	@echo "Cleaning build artifacts..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info
	@rm -rf chargebee.egg-info/
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .mypy_cache/
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete

