from django.core.management.base import BaseCommand
from django.contrib.auth import models as authModels
from django_apptitoso.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):

        CulinaryConcept.objects.get_or_create(name="Al Dente",
                    picture = "uploads/culinaryConcepts/alDente.jpeg",
                    description = "Esse é o ponto de cozimento perfeito para algumas massas e legumes. O alimento fica cozido, mas com uma certa resistência à mordida. Nem muito mole, nem duro demais")

        CulinaryConcept.objects.get_or_create(name="Banho Maria",
                    picture = "uploads/culinaryConcepts/banhoMaria.jpeg",
                    description = "Processo de aquecimento ou cozimento onde mergulha-se o recipiente com o alimento em água fervente, no fogão ou no forno. Isso evita o calor excessivo do contato direto com o fogo e é muito utilizada para derreter chocolate, bater creme de ovos e assar pudins. Uma curiosidade: esse nome foi dado em homenagem à alquimista grega Maria, a Judia, que supostamente inventou o processo")
    
        CulinaryConcept.objects.get_or_create(name="Flambar",
                    picture = "uploads/culinaryConcepts/flambar.jpeg",
                    description = "Durante o preparo de algum alimento, você pode acrescentar bebida alcoólica (conhaque, rum ou uísque) e iniciar um fogo sobre a panela para caramelizar e apurar o sabor da bebida ao prato")

        CulinaryConcept.objects.get_or_create(name="Marinar",
                    picture = "uploads/culinaryConcepts/marinar.jpeg",
                    description = "Deixar a carne em preparação de azeite, vinagre ou vinho para que fique mais saborosa ou macia. O procedimento também pode ser usado em alimentos já cozidos para conservá-los")
        
        CulinaryConcept.objects.get_or_create(name="Redução",
                    picture = "uploads/culinaryConcepts/reducao.jpeg",
                    description = "Muito usada em bifes e assados, a redução de vinho significa que você tem de deixar a bebida em uma panela, em fogo baixo, até o volume dela diminuir à quantidade desejada.")
        
        CulinaryConcept.objects.get_or_create(name="Selar",
                    picture = "uploads/culinaryConcepts/selar.jpeg",
                    description = "É o método que consiste em dourar a carne na panela quente para formar uma crostinha dourada e deixar o alimento molhadinho por dentro")
        
        CulinaryConcept.objects.get_or_create(name="Confit",
                    picture = "uploads/culinaryConcepts/confit.jpeg",
                    description = "Técnica de cozinhar a carne em sua própria gordura. Antes de cozinhar, o alimento passa por um processo de marinada ou cura. Depois de pronto é guardado na gordura do cozimento, que deve ser retirada antes de servir o prato. Também é uma técnica de conservação para frutas e legumes – usando calda de açúcar, aguardente ou vinagre.")

        CulinaryConcept.objects.get_or_create(name="Aromatizar",
                    picture = "uploads/culinaryConcepts/marinar.jpeg",
                    description = "Adicionar ervas, essências, vinhos ou licor a um alimento. É o mesmo que perfumar molhos ou alimentos.")
        
        CulinaryConcept.objects.get_or_create(name="Amaciar",
                    picture = "uploads/culinaryConcepts/amaciar.jpeg",
                    description = "Esse termo é usado para quando queremos deixar a carne mais tenra. Pode ser batendo com um martelo de cozinha, marinando por diferentes períodos de tempo e temperos ou usando produtos próprios para amaciar a carne.")
        
        CulinaryConcept.objects.get_or_create(name="Caramelizar",
                    picture = "uploads/culinaryConcepts/selar.jpeg",
                    description = "Derreter o açúcar em uma panela até que fique totalmente líquido e com sabor de caramelo, formando uma calda.  Não use água. Utilizado para “untar” forma de pudim ou para passar docinhos.")
        
        CulinaryConcept.objects.get_or_create(name="Claras em Neve",
                    picture = "uploads/culinaryConcepts/ClarasNeve.jpeg",
                    description = "Claras muito bem batidas, de maneira que fiquem endurecidas e quando o batedor for levantado elas não caem.")

        CulinaryConcept.objects.get_or_create(name="Empanar",
                    picture = "uploads/culinaryConcepts/empanar.jpeg",
                    description = "uma técnica culinária bastante popular a qual pode ser aplicada em legumes e carnes em geral para conferir crocância, textura e sabor especial à comida.")
        


        Category.objects.get_or_create(name="Recomendação Apptitosa")
        Category.objects.get_or_create(name="Saudável")
        Category.objects.get_or_create(name="Vegetariano")
        Category.objects.get_or_create(name="Vegano")
        Category.objects.get_or_create(name="Para Iniciantes :)")
        Category.objects.get_or_create(name="Doce")
        Category.objects.get_or_create(name="Bolo")
        Category.objects.get_or_create(name="Carne")
        Category.objects.get_or_create(name="Salada")
        Category.objects.get_or_create(name="Frutos do Mar")
        Category.objects.get_or_create(name="Peixe")
        Category.objects.get_or_create(name="Bebida")
        Category.objects.get_or_create(name="Massa")
        Category.objects.get_or_create(name="Barato")
        Category.objects.get_or_create(name="Mexicano")
        Category.objects.get_or_create(name="Japonês")
        Category.objects.get_or_create(name="Europeu")
        Category.objects.get_or_create(name="Asiático")
        Category.objects.get_or_create(name="Barato")
        Category.objects.get_or_create(name="Rende Muito")
        Category.objects.get_or_create(name="Bonito")


        authModels.User.objects.get_or_create(username="vovovo",
                                                    first_name="Betinha",
                                                    last_name="Vovó",
                                                    email="vovozinha@vovo.com")
        
        tempUser = authModels.User.objects.get(username="vovovo")
        tempUser.set_password("senha")

        User.objects.get_or_create(user = tempUser)

        Recipe.objects.get_or_create(name= "Pão de Queijo",
                                    description= "O pão de queijo é a receita perfeita para o seu lanche da tarde! Delicioso, ele combina com o café quentinho ou um suco bem gelado.",
                                    )

        Recipe.objects.get_or_create(name= "Compota de Abacaxi",
                                    description= "Receita de compota de abacaxi, perfumada com especiarias como gengibre, cravo e canela e um toque de cachaça para finalizar.",
                                    )
        
        Recipe.objects.get_or_create(name= "Coxinha Fit",
                                    description= "Coxinha Fit pré treino",
                                    )

        Recipe.objects.get_or_create(name= "Camarão na Moranga",
                                    description= "Aprenda a fazer esta deliciosa receita de Abóbora Moranga recheada com Camarões e creme de leite e prove que esta receita feita em casa é outra coisa!",
                                    )
        