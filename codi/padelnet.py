# Saludar
salutació = ("Bon dia, em dic Padelnet! Com estàs? T'ajudaré tot el possible amb tot lo relacionat amb el pàdel.")
print(salutació)

# Preguntar el Nom
nom = input("Com et dius? ")
print("Hola " + nom + ", encantat de coneixe't!!!")

# Pregunta 1
p1_resposta = input("T'agrada el pàdel? ").lower()

usuari_agrada_padel = "no"

# Resposta segons la primera pregunta
if "si" in p1_resposta:
    print("Oh yeah!")
    usuari_agrada_padel = "si"
else:
    print("Adeu, quan vulguis parlem ;)")

if usuari_agrada_padel == "si":
    # Pregunta 2 i guarda la resposta en jugador
    jugador = input("Quin és el teu jugador preferit? ")

    # Resposta si el jugador és conegut
    if jugador in [
        "Agustin Tapia", "Arturo Coello", "Alejandro Galan", "Federico Chingotto", "Franco Stupaczuk",
        "Juan Lebron", "Miguel Yanguas", "Jorge Nieto", "Martin Di Nenno", "Jon Sanz",
        "Lucas Bergamini", "Francisco Navarro", "Jeronimo Gonzalez", "Pablo Cardona", "Eduardo Alonso",
        "Francisco Guerrero", "Leandro Augsburger", "Javier Garrido", "Juan Tello", "Alejandro Arroyo",
        "Jairo Bautista", "Alejandro Ruiz", "Javier Leal", "Alex Chozas", "Javier Garcia",
        "Javier Barahona", "Juanlu Esbri", "Jose Antonio Diestro", "Leonel Daniel Aguirre", "Maximiliano Sanchez",
        "Inigo Jofre", "Gonzalo Gabriel Alfonso", "Lucas Campagnolo", "Carlos Daniel Gutierrez", "Victor Ruiz",
        "Valentino Gabriel Libaak", "Miguel Deus", "Nuno Deus", "Francisco Manuel Gil", "Jose Jimenez Casas",
        "Pedro Melendez", "Nicolas Suescun", "Diego Ramos", "Gonzalo Rubio", "Ramiro Moyano",
        "Juan Manuel Restivo", "Javier Valdés", "Martin Andornino", "Facundo Dominguez", "Juan Pablo Cozzolino"
    ]:
        print("Guauuu! És un gran jugador!!! És dels millors del món.")
    else:
        print("No el conec gaire, però segur que és un crack!")

    # Pregunta 3
    guanyador = input("Qui creus que guanyarà el pròxim torneig? ")
    print("Interessant! Veurem si tens raó ;)")

    # Pregunta 4
    ultima_pregunta = input("Vols que et recomani unes pales de pàdel segons el teu nivell? ").lower()

    if "si" in ultima_pregunta:
        print("Perfecte! Si estàs començant, et recomano una pala lleugera com Siux o Black Crown. Si ets un nivell intermedi, una mica més dura com Nox o Wilson. I si ja ets professional, una pala híbrida d'atac et pot anar genial!")
    else:
        print("Cap problema! Si canvies d’opinió, t’ajudaré encantat.")

    # Pregunta 5
    saber_més = input("Vols saber alguna cosa més sobre pàdel? ").lower()
    if "si" in saber_més:
        print("És el Josue Hernandez! També va ser un dels grans jugadors quan el pàdel encara no era famós!!!!")
    else:
        print("Cap problema, pots preguntar-me quan vulguis! :)")

    # Pregunta 6
    altra_pregunta = input("Fes qualsevol pregunta sobre pàdel i la respondré! Vols fer-ne alguna ara? ").lower()
    if "si" in altra_pregunta:
        print("El jugador que per més anys ha estat número 1 és Fernando Belasteguín, un jugador que va destacar pel seu globus i la seva bandeja!")
    else:
        print("D’acord! Quan vulguis, podem parlar més sobre pàdel ;)")
