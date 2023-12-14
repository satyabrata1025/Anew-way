from taipy import Gui
value = "stock simulator by satya"
path = "logo.jpeg"
company_name ="TATA"
company_minprice= 200
company_maxprice= 2000


page="""
<|text-center |
<|{path}|image|>

<|{value}|hover_text =welcome to the club|>


Name of stock:<|{company_name}|input|>

Name of min_price:<|{company_minprice}|input|>

Name of max_price:<|{company_maxprice}|input|>



>
 
"""
if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)