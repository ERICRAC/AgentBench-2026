# V2.2 — piloto supervisionado congelado

[Français](V2_2_SUPERVISED.md) · [English (UK)](V2_2_SUPERVISED.en.md) · [Español](V2_2_SUPERVISED.es.md) · **Português**

**Nova autorização: tentativa 002**, calculadora simples Astra médio, do zero. Mesmo motor, mandatos e testes de 001; sem solução anterior. Saldo inicial não medido; go do utilizador após pedido de quota completa. Sem retry ou científica autorizados. [Manifesto 002](v2-2-supervised-002.json).

O utilizador autoriza **apenas a calculadora simples**, Astra médio, ID astra-medium-core-v2-2-supervised-001. Científica e repetições exigem novo acordo. [Manifesto congelado e hashes](v2-2-supervised.json).

Dois papéis, três sessões novas: MAIN implementa, REV-01 revê, MAIN arbitra e corrige. Mantêm-se os [mandatos V2.2](V2_2_PROTOCOL.pt.md); o lançador acrescenta apenas contexto da pasta e comando local do verificador. Sem ajuda humana no código ou consultor adicional. Primeira verificação oficial na fase final; diagnóstico retrospetivo inicial após encerramento.

Pasta temporária nova fora do repositório, cópias intactas do desafio/verificador/testes, solução vazia. CLI nativo: MAIN workspace-write, REV-01 read-only, approval never, web desativada. Sem contornar o sandbox. Delegação proibida por mandato e desativada na configuração, **sem garantia técnica absoluta**. Auditoria de ficheiros/eventos não prova ausência de leituras externas. Sem segredos fornecidos ou soluções anteriores consultadas; proteções globais intactas.

Contexto 200000, compactação 180000 total; limites finais 600/1200/1200 palavras. Sem novo teto acumulado ou garantia de quota. Paragem sem repetição por falha, quota, captura não interpretável ou infração observada. Rastos brutos privados; publicar só texto visível auditado e métricas reais, sem raciocínio privado. Captura local testada; parar se o analisador rejeitar eventos CLI.

O dispositivo MCP reforçado permanece NO-GO. Esta é **outra campanha exploratória**, não certificação retroativa de isolamento ou comparação causal com V1/V2 históricas. Comparação homogénea requer V1 nas mesmas condições.

72 testes de manutenção aprovados antes do lançamento: quatro novos sobre sequência, não reinício, paragem por falha, autorização e argumentos TOML. [Lançador](../scripts/run_v2_2_supervised.py) · [Testes](../tests/test_v2_2_supervised.py).

OpenAI Docs orientou CLI não interativo e captura JSONL. O login local indica ChatGPT; acesso real ao Astra e consumo ainda por observar. [Documentação oficial](https://learn.chatgpt.com/docs/non-interactive-mode).

[README](../README.pt.md) · [Qualificação anterior](../results/v2-2-dispatch.pt.md)
