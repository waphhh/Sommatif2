#J'ai décidé de faire un questionnaire qui m'en dit plus sur la personnalité et les préférences des utilisateurs.
#Voici une de mes questions qui me permettra d'en savoir plus sur les préférences des utilisateurs.
print("Parmi ces 3 émissions, quelle est celle que vous préférez ? : Money Heist, Breaking Bad, Game of Thrones et Aucun.")

émissions = input().lower()
if émissions == "money heist":
     print("Moi aussi, Money Heist était si passionnant, si excitant et m'a tenu en haleine à tout moment")

elif émissions == "breaking bad": 
    print("Ouuuuuu, c'est bien, on apprend beaucoup de cette série et le personnage de Bryan Cranston était tellement incroyable.")

elif émissions == "game of thrones":
    print("The show was amazing but in my opinion the last season didn't meet the expectations.")

elif émissions == "aucun":
    print("C'est normal, tout dépend de ce que vous préférez.")

#Cela permettra de savoir quel est le style de vie de l'utilisateur
print("Si vous deviez choisir un aliment parmi ces 3, lequel serait? : Fast Food, Bonbons or Végétarien.")

food = input().lower()
if food == "fast food":
    print("Oui, je suis d'accord, c'est pas bon pour la sante mais c'est trop bon pour arrêter de manger.")

elif food == "bonbons":
    print("Ils sont si doux et délicieux, mais ils me font parfois mal aux dents.")

elif food == "végétarien":
    print("Ce n'est pas la nourriture la plus savoureuse, mais elle garde le corps en bonne santé.")

#Cela m'aide à comprendre quel est le type de personnalité de l'utilisateur et comment il se sentirait ou agirait dans certaines situations
print("Si quelqu'un prenait la dernière livraison dont vous avez besoin à l'épicerie, comment vous sentiriez-vous? : Heureux, frustré, Triste ou Neutre.")

feel = input().lower()
if feel == "heureux":
    print("Moi aussi, je serais heureux pour eux parce qu'ils en ont peut-être plus besoin que moi.")

elif feel == "frustré":
    print("Moi aussi, j'aurais été en colère parce que j'en avais vraiment besoin ou si je l'avais cherché pendant un certain temps.")

elif feel == "triste":
    print("Moi aussi, je serais triste parce que j'en ai besoin, mais eux aussi en ont besoin.")

elif feel == "neutre":
    print("Moi aussi, je ne ressentirais rien d'autre parce que ce n'est pas si grave qu'ils l'aient obtenu en premier, donc je ne peux pas faire grand-chose à ce sujet.")
#C'est la fin de mon programme ce fut un programme très utile parce qu'il m'a aidé à comprendre d'autres points de vue et opinions