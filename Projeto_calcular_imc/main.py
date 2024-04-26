import flet as ft

def main(page:ft.Page):
    
    def close_banner(e):
        page.banner.open  = False
        page.update()


    def calcular_imc(e):
        alt = altura.value
        pe = peso.value
        page.update()
    
    #Configurando a pagina 



    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora de IMC"),
        #para centralizar usamos o center_title
        center_title=False,
        #define a cor de fundo para "surface"
        bgcolor= ft.colors.GREY
    )
    #Definindo a largura
    page.window_width = 400
    #defininfo a altura
    page.window_height = 550
    #Configurando o banner de notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,color=ft.colors.AMBER,size=40),
        content=ft.Text("OPS, preencha todos os campos !"),
        actions=[
            ft.TextButton("Ok",on_click=close_banner)
        ]
    )

    altura = ft.TextField(label="Altura",hint_text="Digite sua altura")
    peso = ft.TextField(label="Peso",hint_text="Digite seu peso")
    genero = ft.Dropdown(
        label="Genero",
        hint_text="Escolha seu genero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ]
    )
    #BOTAO PARA CALCULAR O IMC
    b_calcular = ft.ElevatedButton(text="CALCULAR O IMC ",bgcolor=ft.colors.WHITE,color=ft.colors.AMBER_800)

    # EXIBIR O RESULTADO DO IMC
    imc = ft.Text("SEU IMC É ...",size=30)
    detalhes = ft.Text("Insira seu dados ",size=20)

    img_capa = ft.Image(
        src=r".\assets\logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            imc,
            detalhes,

        ]   
)
    
    info= ft.Row(
        controls=[
            info_app_resultado,
            img_capa,
        ]
    )



    # Layout da pagina 
    layout = ft.ResponsiveRow (
        [
        ft.Container (
            info,
            # bgcolor =ft.colors.GREY,
            padding=5,
            col={"sm":4,"md":4,"xl":4},
            alignment= ft.alignment.center,

        ),
          ft.Container (
            altura,
            padding=5,
            # bgcolor=ft.colors.WHITE,
            col={"sm":12,"md":3,"xl":3},
            alignment= ft.alignment.center,

        ),
          ft.Container (
            peso,
            padding=5,
            # bgcolor=ft.colors.WHITE,
            col={"sm":12,"md":3,"xl":3},
            alignment= ft.alignment.center,

        ),
          ft.Container (
            genero,
            padding=5,
            # bgcolor=ft.colors.WHITE,
            col={"sm":12,"md":3,"xl":3},
            alignment= ft.alignment.center,

        ),
        
          ft.Container (
            b_calcular,
            padding=5,
            # bgcolor=ft.colors.WHITE,
            col={"sm":12,"md":3,"xl":3},
            alignment= ft.alignment.center,

        ),

        ]
    )
    page.add(layout)
    page.add(img_capa)

ft.app(target=main)