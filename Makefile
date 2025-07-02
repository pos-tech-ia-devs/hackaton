run:
	python3 -m src.main

install-requirements:
	pip install -r requirements.txt

.PHONY: install
LIBS=
install:
	@if [ -z "$(LIBS)" ]; then \
		echo "Erro: Nenhuma biblioteca especificada."; \
		echo "Uso: make install LIBS=\"<biblioteca1> <biblioteca2> ...\""; \
		exit 1; \
	fi
	@echo "--> Instalando bibliotecas: $(LIBS)..."
	@pip install $(LIBS) && pip freeze > requirements.txt
	@echo "--> Instalação concluída e requirements.txt atualizado com sucesso."

