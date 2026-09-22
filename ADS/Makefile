.PHONY: check demo inventory clean
check:
	python3 -m compileall -q .
	python3 03-qualidade-de-software/test_calculadora.py

demo:
	bash scripts/run_examples.sh

inventory:
	python3 scripts/inventory.py

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
