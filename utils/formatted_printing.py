from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Frame, Box
from prompt_toolkit.layout.containers import VSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from builtins import map
from prompt_toolkit.layout import HorizontalAlign
from utils.color_palette import Colors
import pandas as pd
from collections import defaultdict
import os
from utils.formatting import combine_dicts

"""
Formats and prints items. Either single item or multiple
items as a table. The function for table printing is quite
messy. Have not yet found an elegant way to simplify it.
"""
class CerealPrinter(object):
    
    
    @staticmethod
    def print_table_of_cereal(cereal: list[dict]):
        
        table = combine_dicts(cereal)
        list_c = list(table.values())
        for l in list_c:
            print(l)
        # nrs = [(Colors.LightGrey, f" \n\n")]
        # names = [(Colors.LightGrey, f"name\n\n")]
        # prices = [(Colors.LightGrey, f"price $\n\n")]
        # counts = [(Colors.LightGrey, f"count\n\n")]
        # categories = [(Colors.LightGrey, f"category\n\n")] 
        # ids = [(Colors.Grey, f"id\n\n")] 
        
        # nr = 0
        # for result in sorted(items, key= lambda x: x.category):
        #     nr += 1
            
        #     nrs.append( (Colors.LightGrey, f"{nr}\n") )
        #     names.append( (Colors.LightBlue, f"{result.name}\n") )
        #     prices.append( (Colors.MutedGreen, f"{str(result.price)}\n") )
        #     counts.append( (Colors.MutedYellow, f"{str(result.count)}\n") )
        #     categories.append( (Colors.LightGrey, f"{str(result.category)}\n") )
        #     ids.append( (Colors.Grey, f"{result.id}\n") )
            
        
        # info = [ nrs, names, prices, counts, categories, ids ]
        # formatted = map(lambda x: FormattedText(x), info)
        ftc = map(lambda x: FormattedTextControl(x), list_c)
        print("ftc")
        wins = list(map(lambda x: Window(x,dont_extend_width=True), ftc))
        print(wins)
        
        body = VSplit( wins, align=HorizontalAlign.LEFT, padding=1)
        print_container(body)
        print(body)
        # termw = os.get_terminal_size().columns
        # print(termw)
        # pref = body.preferred_width(termw)
        # print(pref)
        # body.width = body.preferred_width( termw ).preferred
        # print(body.width)
        print("preinner")
        inner_box = Box(body, padding_left=2, padding_right=2)
        print_container(inner_box)
        print("preframe")
        
        frame = Frame(inner_box)

        print("prebox")
        
        box = Box(frame, padding_left=1)

        print("preprint")
        print_container(box)
    