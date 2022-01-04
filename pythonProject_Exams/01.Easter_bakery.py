flour = float(input())
kg_flour = float(input())
sugar = float(input())
eggs = int(input())
maya = int(input())

kg_sugar = flour-flour*0.25
kora_eggs = flour+flour*0.10
maya_packet = kg_sugar-kg_sugar*0.80

sum_flour=flour*kg_flour
sum_sugar = sugar*kg_sugar
sum_eggs=eggs*kora_eggs
sum_maya=maya*maya_packet
total = sum_flour+sum_sugar+sum_eggs+sum_maya
print(f'{total:.2f}')