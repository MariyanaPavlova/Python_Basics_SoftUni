name = input()
tickets_adults = int(input())
ickets_kids = int(input())
net_adult = float(input())
taksa = float(input())

net_kid = net_adult - net_adult * 0.70
price_ticket_adult = net_adult + taksa
price_ticket_kid = net_kid + taksa
total_price = (tickets_adults * price_ticket_adult) + (ickets_kids * price_ticket_kid)
profit = total_price * 0.20
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")

