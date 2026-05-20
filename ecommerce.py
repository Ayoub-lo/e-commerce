import json

cartList = []
listProduit = []


def menu():
    print("""
    1) Ajouter au panier
    2) afficher le contenue du panier
    3) Retirer un Produit
    4) valider la commande
    5) quitter
    """)


def addToCart():
    produitNum = input("donner le nombre du produit : ")
    produitQuantity = int(input("choisir une quantity: "))
    with open("produits.json", "r", encoding="utf-8") as file:
        listProduit = json.load(file)
        product = listProduit[produitNum]
        product["quantity"] = produitQuantity
        cartList.append(product)


def afficher():
    print("""
========== votre cart ==========
""")
    if len(cartList) == 0:
        print("aucun to afiche")
        return

    for i in range(len(cartList)):
        print(f"""
Nom : {cartList[i]["nom"]}
Quantity : {cartList[i]["quantity"]}
""")


def removeItemCart():
    afficher()
    if len(cartList) == 0:
        return
    index = int(input("donner index du produit à supprimer : "))
    if index >= 0 and index < len(cartList):
        cartList.pop(index)
        print("Produit supprime")
    else:
        print("donner correct ")


def validerCommande():
    print("""
===== command valid =====
""")
    if len(cartList) == 0:
        print("aucune dans panier ")
        return
    for item in cartList:
        print(f"{item['nom']} x {item['quantity']}")
    print("Commande validée ")
    cartList.clear()




while True:
    menu()
    menuInput = int(input("donner votre choix : "))
    if menuInput == 1:
        addToCart()
    elif menuInput == 2:
        afficher()
    elif menuInput == 3:
        removeItemCart()
    elif menuInput == 4:
        validerCommande()
    elif menuInput == 5:
        print("quitter")
        break
    else:
        print("enter un nombre de 1 a 5")