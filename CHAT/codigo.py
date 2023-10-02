import flet as ft


def main(pagina):
    texto = ft.Text("JP Zat-Zat")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome:")

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(ft.Row(
                [campo_msg, botao_enviar_msg ]
        ))
        pagina.update()

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))

        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no Zat-Zat",
                                 size=12,
                                 italic=True,
                                 color=ft.colors.ORANGE_600
                                 ))

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_msg.value,
                                "usuario": nome_usuario.value, 
                                "tipo": "mensagem"
                                })
        campo_msg.value = ""
        pagina.update()

    campo_msg = ft.TextField(label="Digite uma mensagem:", on_submit=enviar_mensagem)
    botao_enviar_msg = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao JP Zat-Zat"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)


    pagina.add(texto)
    pagina.add(botao_iniciar)



# ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
ft.app(target=main)