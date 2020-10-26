#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prod = float(input(f'Preço do produto: '))
desc = 5 / 100 * prod
final = prod - desc
print(f'O valor final do produto na promoção com 5% de desconto é R${final:.2f}.')
