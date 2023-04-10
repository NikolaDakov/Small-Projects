age_lily = int(input())
price_w_m = float(input())
price_toy = int(input())

diff = 0
money = 10
money_form_gifs = 0

for num in range(1, age_lily + 1):]
    if num % 2 == 0:
        money_form_gifs += money - 1
        money += 10
    else:
        money_form_gifs += price_toy

diff = abs(money_form_gifs - price_w_m)
if money_form_gifs >= price_w_m:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
