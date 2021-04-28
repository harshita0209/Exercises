from model_solution import Match
from view_solution import retrive_country,retrive_sport,display
sport=['Football','Basketball','Hockey','Cricket']
country=['USA','New Zealand','England','India']
match_data={"sport":sport,"country":country}
data_list=Match(match_data)
show=data_list.get_list(match_data)
sport=retrive_sport()
country=retrive_country()
result=data_list.retrive_match(sport,country,match_data)
display(result)

