import logging

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
    handlers=[
        logging.FileHandler("helloflask.log", mode='w'),
        logging.StreamHandler()
    ]
)

# Agora, você pode usar o logger padrão para logar mensagens
logger = logging.getLogger(__name__)

# Exemplo de uso do logger
logger.info("Logger configurado com sucesso.")
