# Títuli: Chat
# Botão de iniciar chat
    # popup (janela na frente da tela)
    # Título: Bem vindo ao Chat
    # Campo de texto -> Escreva seu nome no chat
    # Botão: Entrar no chat
        # sumir com o título Chat
        #sumir com o botão "Iniciar chat"
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas
            # Campo: Digite sua mensagem
            # Botão de enviar

# importar o flet
import flet as ft

# criar a função principal do seu aplicativo
def main(pagina):
    # criar todas as funcionalidades
    
    #criar o elemnto
    titulo = ft.Text('Chat')
    
    titulo_janela = ft.Text('Bem vindo ao Chat')
    
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        texto_entrar_chat = ft.Text(f'{campo_nome_usuario.value} entrou no chat')
        chat.controls.append(texto_entrar_chat)
        pagina.update()

    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat', on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)

    # adicionar o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o aplicativo
ft.app(main)