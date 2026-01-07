# 🤖 Ragnarok Discord Bot

Um bot Discord que integra o scraper do Ragnarok, permitindo buscar informações de itens direto no Discord.

## 📋 Requisitos

- Python 3.8+
- Token de bot Discord
- Permissões necessárias no servidor Discord

## 🔧 Instalação

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar o token do Discord

Crie um arquivo `.env` na raiz do projeto:

```
DISCORD_TOKEN=seu_token_aqui
OWNER_ID=seu_discord_id_aqui
```

**Como obter o token:**
1. Vá para [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application"
3. Dê um nome ao seu bot
4. Vá para "Bot" → "Add Bot"
5. Copie o token em "TOKEN"
6. Cole no arquivo `.env`

**Como obter seu Discord ID:**
1. Ative "Developer Mode" no Discord (User Settings → Advanced → Developer Mode)
2. Clique com botão direito em seu nome
3. Clique em "Copy User ID"
4. Cole no arquivo `.env` como `OWNER_ID`

### 3. Configurar permissões do bot

Vá para OAuth2 → URL Generator e selecione:
- **Scopes:** `bot`
- **Permissions:** 
  - Send Messages
  - Embed Links
  - Read Messages/View Channels

Copie a URL gerada e abra em seu navegador para adicionar o bot ao seu servidor.

## 🚀 Execução

### Opção 1: Execução Simples
```bash
python discord_bot.py
```

### Opção 2: Com Restart Automático (Recomendado)

**Windows (PowerShell):**
```powershell
.\run_bot.ps1
```

**Windows (CMD):**
```cmd
run_bot.bat
```

**Linux/Mac:**
```bash
bash run_bot.sh
```

O bot será reiniciado automaticamente quando encerrar ou quando você usar o comando `/restart`.

## 🔄 Comando de Restart

Use o comando `/restart` para reiniciar o bot com as novas modificações:

```
/restart
```

⚠️ **Apenas o proprietário (definido em OWNER_ID) pode usar este comando.**

## 📖 Comandos Disponíveis

### `/item <item_id>`
Busca informações de um item no Ragnarok

**Exemplo:**
```
/item 547
```

**Retorna:**
- Nome da loja
- Nível de refino
- Quantidade em ROP
- Tipo de valor
- Quantidade disponível

### `/help_ragnarok`
Mostra a lista de comandos disponíveis

## 📁 Estrutura do Projeto

```
ScraperRagnarok/
├── scraper_ragnarok.py      # Scraper principal
├── discord_bot.py            # Bot Discord
├── requirements.txt          # Dependências Python
├── .env                       # Token do bot (não commitar!)
├── .env.example              # Exemplo de .env
└── output.html               # Saída HTML (gerada)
```

## 🔐 Segurança

- ⚠️ **NUNCA** compartilhe seu `DISCORD_TOKEN`
- Sempre use `.env` para armazenar credenciais
- Adicione `.env` ao `.gitignore` se estiver versionando

## 🛠️ Troubleshooting

### Bot não responde?
- Verifique se o token está correto no `.env`
- Confirme que o bot foi adicionado ao servidor
- Verifique as permissões do bot no servidor

### Erro de conexão?
- Verifique sua internet
- Tente reiniciar o bot
- Consulte o console para mais detalhes

### Item não encontrado?
- Verifique se o ID do item está correto
- Confirme que o site do Ragnarok está acessível

## 📝 Notas

- O bot usa slash commands (`/comando`)
- As informações são buscadas em tempo real do site
- Suporta múltiplas lojas por item

## 🤝 Contribuições

Sinta-se livre para fazer melhorias no código!

---

Desenvolvido com ❤️ para a comunidade Ragnarok
