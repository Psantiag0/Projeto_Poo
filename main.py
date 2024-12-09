import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Reservas de Hotel"
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Quartos",
                content=ft.Container(
                    width=50,
                    height=50,
                    margin=30,
                    padding=10,
                    content=ft.Column([ft.Text("Adicionar Quartos"),
                    ft.TextField(label="Número do Quarto"),
                    ft.Dropdown(
                        label="Tipo do Quarto",
                        options=[
                        ft.dropdown.Option("Suíte Simples"),
                        ft.dropdown.Option("Suíte Dupla"),
                        ft.dropdown.Option("Suíte Presidencial"),
                        ]),
                    ft.TextField(label="Preço da Diária"),
                    ft.ElevatedButton(text="Adicionar Quarto", width=150),

                    ]),
                ),
            ),
            ft.Tab(
                text="Clientes",
                
                content=ft.Container(
                    width=50,
                    height=50,
                    margin=30,
                    padding=10,
                    content=ft.Column([ft.Text("Adicionar Clientes"),
                    ft.TextField(label="Nome do cliente"),
                    ft.TextField(label="CPF do cliente"),
                    ft.TextField(label="Telefone do cliente"),
                    ft.ElevatedButton(text="Adicionar Cliente", width=150),
                    
                    ]),
                ),
            ),
            ft.Tab(
                text="Reservas",
                content=ft.Container(
                    width=50,
                    height=50,
                    margin=30,
                    padding=10,
                    content=ft.Column([ft.Text("Controle de Reservas"),
                    ft.TextField(label="Número do Quarto"),
                    ft.ElevatedButton(text="Adicionar Reserva", width=150),
                    
                    ]),
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)

ft.app(main)