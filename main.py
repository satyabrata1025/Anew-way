from taipy import Gui
value= "stock simulator by satya"
page="""
<|text-center |
<|{value}|hover_text =welcome to the club|>
>
 
 
"""
if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)