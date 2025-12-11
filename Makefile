# ============================
# Lead Sniper — Makefile
# ============================

VENV_BIN=venv/bin

.PHONY: run install clean format

# ----------------------------
# Установка зависимостей
# ----------------------------
install:
	$(VENV_BIN)/pip install -r requirements.txt
	$(VENV_BIN)/pip freeze > requirements.txt

# ----------------------------
# Запуск основного пайплайна
# ----------------------------
run:
	$(VENV_BIN)/python -m src.main
