### Guia prático de como usar/testar este repositório na sua máquina (Ubuntu + VScode)

#### Clonando este repositório para sua máquina 
  escolha um diretório e utilize este comando no terminal:
  
     $ git clone git@github.com:ignizxl/helloflask.git

#### Abrindo o projeto na sua ide (de preferência use VScode):
  informe o path onde o repositório foi clonado e digite o seguinte comando:
  
    $ path/helloflask code .

#### Criando uma vm (Virtual Machine):
  no terminal, dentro do seu projeto digite o seguinte comando:
     
     $ sudo apt install python3-virtualenv

     $ virtualenv venv
  
  ou, se preferir

     $ sudo apt install python3.12-venv 

     $ python3 -m venv venv

#### Ativando o nosso ambiente virtual:
  para ativar o ambiente virtual digite o seguinte comando:

    $ source venv/bin/activate

####  Fazendo a instância do banco:
  para instanciar o banco utilize o seguinte comando:
    
    $ python3 ddl.py

#### Flask run:
  depois de seguir esses passos, finalmente podemos rodar o projeto utilizando o comando:

    $ flask run

  ou, se preferir

    $ flask run --debug