@echo off
set AMBIENTE_VIRTUAL=.venv
python -m venv %AMBIENTE_VIRTUAL%
echo Ambiente virtual criado com sucesso.
call .\%AMBIENTE_VIRTUAL%\Scripts\activate
pip install flet
echo Libs instaladas
echo Ambiente virtual foi configurado!
echo Inicializando o projeto
call flet run .\Projeto_calcular_imc\main.py