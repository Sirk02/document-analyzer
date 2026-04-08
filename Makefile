# Makefile for the Document Processing Service

# ==============================================================================
# HELP
# ==============================================================================
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install          Install all backend and frontend dependencies"
	@echo "  run-backend      Start the backend FastAPI server (requires separate terminal)"
	@echo "  run-frontend     Start the frontend React dev server (requires separate terminal)"
	@echo "  test-backend     Run backend Python tests"
	@echo "  test-frontend    Run frontend React tests"
	@echo ""
	@echo "Example Workflow:"
	@echo "1. Run 'make install' to set everything up."
	@echo "2. In terminal 1, run 'make run-backend'."
	@echo "3. In terminal 2, run 'make run-frontend'."

# ==============================================================================
# INSTALLATION
# ==============================================================================
.PHONY: install-backend install-frontend install
install-backend:
	@echo "Installing backend Python dependencies..."
	@python3 -m venv backend/venv
	@backend/venv/bin/pip install -r backend/requirements.txt
	@echo "Backend dependencies installed."

install-frontend:
	@echo "Installing frontend Node.js dependencies..."
	@cd frontend && npm install
	@echo "Frontend dependencies installed."

install: install-backend install-frontend

# ==============================================================================
# RUNNING THE APPLICATION
# ==============================================================================
.PHONY: run-backend run-frontend
run-backend:
	@echo "Starting backend FastAPI server on http://127.0.0.1:8000..."
	@cd backend && venv/bin/uvicorn src.main:app --reload

run-frontend:
	@echo "Starting frontend React dev server on http://localhost:3000..."
	@cd frontend && npm start

# ==============================================================================
# TESTING
# ==============================================================================
.PHONY: test-backend test-frontend
test-backend:
	@echo "Running backend Python tests..."
	@cd backend && venv/bin/pytest

test-frontend:
	@echo "Running frontend React tests..."
	@cd frontend && npm test
