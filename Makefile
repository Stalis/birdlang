PYTHON_EXE := python3
venv_folder = .venv

.PHONY: tests
tests:
	$(PYTHON_EXE) main.py ./testdata/main.zl -o ./testdata/output

.PHONY: pep8
pep8:
	yapf -e '$(venv_folder)/*' -r -i -vv .