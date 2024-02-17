
class tintas2:
    def __init__(self):
        print("Bem-vindo ao Calculador de Latas de Tinta!")
        largura = float(input("Informe a largura da parede em metros: "))
        altura = float(input("Informe a altura da parede em metros: "))

        # Calcula a área da parede
        areaParede = largura * altura

        latas_inteiro = areaParede // 3
        latas_resto = areaParede% 3 > 0
        latas_total = latas_inteiro + latas_resto

        # Exibindo o resultado
        print('Para pintar uma parede de ' + str(largura) + ' m x ' + str(largura) + ' m, você precisará de ' +  str(latas_total) + ' latas de tinta.')

call_tintas2 = tintas2()