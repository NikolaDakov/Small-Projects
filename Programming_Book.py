price_page = float(input())
price_cover = float(input())
discount_paper = float(input())
salary_designer = float(input())
percent_team = float(input())

total_page = price_page * 899
total_cover = price_cover * 2
total_paper = (total_page + total_cover) - (discount_paper/100 * (total_page + total_cover))
total_design = total_paper + salary_designer
total = total_design - (percent_team/100 * total_design)
print(f'Avtonom should pay {total:.2f} BGN.')
