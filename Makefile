lint:
	flake8 . --exclude ./venv/ --count --max-complexity=10 --max-line-length=127 --statistics
	