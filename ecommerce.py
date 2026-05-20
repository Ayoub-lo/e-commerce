# print(cartList[0]["nom"]  , cartList[0]["quantity"])

# with open("produits.json","r",encoding="utf-8") as file:
#         listProduit=json.load(file)
import json



def menu():
        print("""
        1) Ajouter au panier
        2) affichier le contenue du panier
        3) Retier un Produit 
        4) valider la commande
        """)

menu()

menuInput  = int(input("donner votre choix : "))



cartList= []
listProduit =[]



def addToCart():
        produitNum = input("donner le nombre  du produit :  ")
        produitQuantity = int(input("choisir un quantity: "))
        with open("produits.json","r",encoding="utf-8") as file:
                listProduit=json.load(file)
                cartList.append(listProduit[produitNum])
                listProduit[produitNum]["quantity"] = produitQuantity

# addToCart(produitNum)


def afficherCart():
        for i in range(len(cartList)):
                print(cartList[i]["nom"] , cartList[i]["quantity"])
afficherCart()
if menuInput == 1 :addToCart()
if menuInput == 2 :afficherCart()






