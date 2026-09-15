import logging
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (.env) na inicialização
load_dotenv()

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] MINDOS: %(message)s"
)
logger = logging.getLogger("MINDOS")

from mindos.graph import create_mindos_graph

def run_mindos(objective: str):
    logger.info("🚀 Iniciando execução do MINDOS MVP...")
    graph = create_mindos_graph()
    initial_state = {"objective": objective}
    final_state = graph.invoke(initial_state)
    return final_state

if __name__ == "__main__":
    objective = "Desenvolver o agente orquestrador do MINDOS"
    run_mindos(objective)