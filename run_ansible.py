import subprocess
import sys

def executar_playbook_ansible():
    """
    Executa o playbook Ansible com o inventário especificado.
    """
    # Define os comandos e argumentos
    comandos_ansible = [
        "ansible-playbook main.yml -i inventario_vagrant.yml"
    ]
    print("Iniciando a execução do playbook Ansible...")
    
    try:
        # Executa o comando e captura a saída
        processo = subprocess.run(comandos_ansible, check=True, capture_output=True, text=True)
        
        # Se a execução foi bem-sucedida (check=True)
        print("\n--- Execução Concluída com Sucesso ---")
        print(processo.stdout)
        
    except FileNotFoundError:
        # Se o comando 'ansible-playbook' não foi encontrado
        print("\n--- ERRO ---")
        print("Ansible não encontrado. Por favor, certifique-se de que está instalado e no seu PATH.")
        sys.exit(1)
        
    except subprocess.CalledProcessError as e:
        # Se o comando falhou com um código de retorno diferente de zero
        print("\n--- ERRO NA EXECUÇÃO ---")
        print(f"O playbook falhou com o código de retorno: {e.returncode}")
        print("\nSaída de Erro (stderr):")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    executar_playbook_ansible()