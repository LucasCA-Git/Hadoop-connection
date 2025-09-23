#!/bin/bash

# comando ansible
COMMAND="ansible-playbook main.yml -i inventario_vagrant.yml"

echo "Executando: $COMMAND"

# executa o ansible-playbook
OUTPUT=$($COMMAND 2>&1)
STATUS=$?

# mostra a saída
echo "=== SAÍDA ==="
echo "$OUTPUT"

# verifica status
if [ $STATUS -eq 0 ]; then
    echo "✅ Playbook executado com sucesso!"
else
    echo "❌ Erro ao executar playbook."
fi
