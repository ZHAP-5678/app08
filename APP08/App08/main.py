import flet as ft


def main(page: ft.page):
    
    
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="mictlan"
    page.fgcolor="gray"
    
    intro=ft.Audio(src="intro mp3",volume=1,balance=8)
    page.overlay.append(intro)
    
    PrimerNivel1=ft.Audio(src="primer_nivel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel1)
    
    SegundoNivel=ft.Audio(src="primer_nivel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel1)
    
    TercerNivel=ft.Audio(src="tercer_nivel.mp3",volume=1,balance=0)
    page.overlay.append(tercernivel)
    
    Cuarto0Nivel=ft.Audio(src="cuarto_nivel.mp3",volume=1,balance=0)
    page.overlay.append(cuartonivel)
    
    QuintoNivel=ft.Audio(src="quinto_nivel.mp3",volume=1,balance=0)
    page.overlay.append(QuintoNivel)

    SextoNivel=ft.Auido(src="sexto_nivel.mp3",volume=1,balance=0)
    page.ovelay.append(quintonivel)

    SeptimoNivel=ft.Audio(src="septimo_nivel.mp3",volume=1,balance,=0)
    page.overlay.append(sextonivel)

    OctavoNivel=ft.Audio(src="octavo_nivel.mp3",volume=1,balance=0)
    page.overlay.append(octavonivel)

    NovenoNivel=ft.Audio(src"noveno_nivel.mp3",volume=1,balance=0)
    page.overlay.append(novenonivel)


btnintro=ft.FilledButton(Text="escuchar el intro", disabled=False)

btnNivel1=ft.ElevatedButton(Text="primer nivel")
img=ft.Image(src"primer-nivel.jpeg", width=150, height=150)

btnNivel2=ft.ElevatedButton(Text="segundo nivel")
img=ft.Image(src"segundo-nivel.jpeg", width=150, height=150) 

btnNivel3=ft.ElevatedButton(Text="tercer nivel")
img=ft.Image(src"tercer-nivel.jpeg", width=150, heigth=150)

btnNivel=ft.ElevatedButton(Text="cuarto nivel")
img=ft.Image(src"cuarto-nivel.jpeg", width=150, heigth=150)