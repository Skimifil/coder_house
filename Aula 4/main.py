from plyer import notification
from datetime import datetime


# Eu separei a chamado da notificação e a notificação em si, assim eu posso tratar o nível da notificação e chamar o
# "notify" uma única vez.
def alerta(nivel, base, etapa):
    if nivel == 1:
        titulo = "Alerta Baixo"
        call_notification(titulo, base, etapa)

    elif nivel == 2:
        titulo = "Alerta Médio"
        call_notification(titulo, base, etapa)

    elif nivel == 3:
        titulo = "Alerta Alto"
        call_notification(titulo, base, etapa)

    # Nãos ei bem se é uma boa prática nesse caso, mas coloquei um erro caso fosse colocado um nivel errado
    else:
        raise ValueError("Nível inválido, deve ser 1, 2 ou 3")


# Dai a notificação em si esta ema função única, que chamo apenas uma vez.
def call_notification(titulo, base, etapa):
    now = datetime.now()
    notification.notify(
        title=titulo,
        message=f"Falha no carregamento da base {base} na etapa {etapa} \n {now}",
        app_name="Nome do aplicativo",
        timeout=10
    )


# Chamo a função de "alerta" e ela que chama a da notificação
try:
    alerta(1, "CLIENTE", "EXTRACAO")
except ValueError as e:
    print(f"Erro: {e}")
