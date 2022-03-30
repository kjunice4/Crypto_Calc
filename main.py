# Crypto Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Crypto Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 

""")
#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
                    
            Button:
                font_size: 75
                background_color: 0, 1, 0, 1
                size_hint_y: None
                height: 200
                text: "Crypto Profit Calculator"
                padding: 10, 10
                on_release:
                    app.root.current = "Crypto_Calc"
                    root.manager.transition.direction = "left" 

            Button:
                font_size: 75
                background_color: 0, 0, 1, 1
                size_hint_y: None
                height: 200
                text: "Crypto Price Calculator"
                padding: 10, 10
                on_release:
                    app.root.current = "Crypto_Price_Calc"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                text: "Crypto Value Calculator"
                padding: 10, 10
                on_release:
                    app.root.current = "Quantity_Calc"
                    root.manager.transition.direction = "left" 
            
            Button:
                font_size: 75
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                text: "Crypto Tips"
                padding: 10, 10
                on_release:
                    app.root.current = "Crypto_Tips"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                padding: 10, 10
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
                
""")
#Price
Builder.load_string("""
<Crypto_Price_Calc>
    id:Crypto_Price_Calc
    name:"Crypto_Price_Calc"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Crypto Price Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        mkt_cap.text = ""
                        supply.text = ""
                        list_of_steps.clear_widgets()     
                        
            TextInput:
                id: mkt_cap
                text: mkt_cap.text
                hint_text: "Market Capital: $"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10

            TextInput:
                id: supply
                text: supply.text
                hint_text: "Circulating Supply: "
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            Button:
                id: steps
                text: "Calcualte"   
                font_size: 60
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 100
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Crypto_Price_Calc.calculate(mkt_cap.text + "&" + supply.text)           
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                       

""")
#Profit
Builder.load_string("""
<Crypto_Calc>
    id:Crypto_Calc
    name:"Crypto_Calc"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Crypto Profit Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        capital.text = ""
                        price.text = ""
                        gains.text = ""
                        list_of_steps.clear_widgets()     
                        
            TextInput:
                id: capital
                text: capital.text
                hint_text: "Capital: $"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: price
                text: price.text
                hint_text: "Crypto Price: $"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                input_filter: "float"
                
            TextInput:
                id: gains
                text: gains.text
                hint_text: "Capital Gains Goal: $"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10

            Button:
                id: steps
                text: "Calcualte"   
                font_size: 60
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 100
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Crypto_Calc.calculate(capital.text + "&" + price.text + "@" + gains.text)           
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")
#Quantity
Builder.load_string("""
<Quantity_Calc>
    id:Quantity_Calc
    name:"Quantity_Calc"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Crypto Value Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        quantity.text = ""
                        price.text = ""
                        list_of_steps.clear_widgets()     
                        
            TextInput:
                id: quantity
                text: quantity.text
                hint_text: "Quantity: #"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: price
                text: price.text
                hint_text: "Crypto Price: $"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                input_filter: "float"
                
            Button:
                id: steps
                text: "Calcualte"   
                font_size: 60
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 100
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Quantity_Calc.calculate(quantity.text + "&" + price.text)           
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")
#Tips
Builder.load_string("""
<Crypto_Tips>:
    id: Crypto_Tips
    name: "Crypto_Tips"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Button:
                font_size: 75
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                text: "Menu"
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Crypto Tips"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "1) Do your research before buying"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "2) Only invest in what you can afford to lose"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "3) Understand the difference between Hot/Cold wallets"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "4) Transfers require gas/network fees"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "5) Do not share your wallet's private keys socially"
                    
""")

#Profit
class Crypto_Calc(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Crypto_Calc, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        def _key_handler(self, instance, key, *args):
            print("Key: ",key)
            print("Current",sm.current)
            if int(key) == 27:
                if sm.current == "Homepage":
                    pass
                elif sm.current == "Menu":
                    pass
                elif sm.current == "Crypto_Calc":
                    sm.transition.direction = 'right'
                    sm.current = "Menu"
                return True
            
    layouts = []
    def calculate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
                
            amp_index = entry.find("&")
            print("amp_index",amp_index)
            
            a_index = entry.find("@")
            print("a_index",a_index)
            
            capital = entry[:amp_index]
            print("capital",capital)
            
            self.ids.list_of_steps.add_widget(Label(text= "Capital: $" + "{:,.2f}".format(float(capital)),font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            crypto_price = entry[amp_index+1:a_index]
            print("crypto_price",crypto_price)
            
            if float(crypto_price) > 1:
                crypto_price = "{:,.2f}".format(float(crypto_price))
                print("crypto_price formatted",crypto_price)
                
            self.ids.list_of_steps.add_widget(Label(text= "Crypto Price: $" + str(crypto_price),font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            capital_goal = entry[a_index+1:]
            print("capital_goal",capital_goal)
            
            self.ids.list_of_steps.add_widget(Label(text= "Capital Gains Goal: $" + str("{:,.2f}".format(float(capital_goal))),font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #Display Target selling price, percent gain to reach capital goal
            
            supply = float(capital) / float(str(crypto_price).replace(",",""))
            print("supply",supply)

            self.ids.list_of_steps.add_widget(Label(text= "Amount of coins you own: " ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= str("{:,}".format(supply)),font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            sell_price = str(float(capital_goal) / supply)
            print("sell_price",sell_price)
            
            if float(sell_price) > 1:
                "{:,.2f}".format(float(sell_price))

            self.ids.list_of_steps.add_widget(Label(text= "Selling price to achieve Capital Gains Goal: ",font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "$" + str(sell_price),font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "To The Moon!" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Crypto_Price_Calc(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Crypto_Price_Calc, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        def _key_handler(self, instance, key, *args):
            print("Key: ",key)
            print("Current",sm.current)
            if int(key) == 27:
                if sm.current == "Homepage":
                    pass
                elif sm.current == "Menu":
                    pass
                elif sm.current == "Crypto_Price_Calc":
                    sm.transition.direction = 'right'
                    sm.current = "Menu"
                return True
    
    layouts = []
    def calculate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            
            amp = entry.find("&")
            print("amp",amp)
            
            mkt_cap = entry[:amp]
            print("mkt_cap",mkt_cap)
            
            supply = entry[amp+1:]
            print("supply",supply)
            
            price = float(mkt_cap) / float(supply)
            print("price",price)
            
            self.ids.list_of_steps.add_widget(Label(text= "Market Capital:" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "$"+"{:,.2f}".format(float(mkt_cap)) ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "÷" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Circulating Supply: " ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "#"+ "{:,.2f}".format(float(supply)) ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "=" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Crypto Price: $" + "{:,.2f}".format(price) ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Quantity_Calc(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Quantity_Calc, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        def _key_handler(self, instance, key, *args):
            print("Key: ",key)
            print("Current",sm.current)
            if int(key) == 27:
                if sm.current == "Homepage":
                    pass
                elif sm.current == "Menu":
                    pass
                elif sm.current == "Quantity_Calc":
                    sm.transition.direction = 'right'
                    sm.current = "Menu"
                return True

            
    layouts = []
    def calculate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            
            amp_index = entry.find("&")
            print("amp_index",amp_index)
            
            quantity = entry[:amp_index]
            print("quantity",quantity)
            
            price = entry[amp_index+1:]
            print("price",price)
            
            self.ids.list_of_steps.add_widget(Label(text= "Quantity: # " + "{:,.2f}".format(float(quantity)),font_size = 50, size_hint_y= None, height=100))
            
            if float(price) > 1:
                price_display = "{:,.2f}".format(float(price))
            else:
                price_display = price

            self.ids.list_of_steps.add_widget(Label(text= "Crypto Price: $" + str(price_display),font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #Display $ Value
            value = float(quantity) * float(str(price).replace(",",""))
            print("value",value)
            
            self.ids.list_of_steps.add_widget(Label(text= "Value: " + "${:,.2f}".format(float(value)),font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "To The Moon!" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)

class Crypto_Tips(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Crypto_Tips, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        print("Key: ",key)
        print("Current",sm.current)
        if int(key) == 27:
            if sm.current == "Homepage":
                pass
            elif sm.current == "Menu":
                pass
            else:
                sm.transition.direction = 'right'
                sm.current = "Menu"
            return True

class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            


sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Crypto_Calc(name="Crypto_Calc"))
sm.add_widget(Crypto_Price_Calc(name="Crypto_Price_Calc"))
sm.add_widget(Quantity_Calc(name="Quantity_Calc"))
sm.add_widget(Crypto_Tips(name="Crypto_Tips"))
sm.current = "Homepage"   


class Crypto_Calc(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Crypto_Calc().run()
