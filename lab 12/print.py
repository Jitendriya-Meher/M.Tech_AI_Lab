supply = {"VLS":0,"LS":20,"MS":40,"HS":60,"VHS":80}
demand = {"LD":25,"MD":50,"HD":75}
price = {"VLPG":10,"LPG":25,"MPG":45,"HPG":60,"VHPG":80}
def mf_supply(x):
    if 0 <= x <= 20: return [{"val":(20-x)/20,"s":"VLS",},{"val":x/20,"s":"LS"}]
    elif 20 < x <= 40: return [{"val":(40-x)/20,"s":"LS",},{"val":(x-20)/20,"s":"MS"}]
    elif 40 < x <= 60: return [{"val":(60-x)/20,"s":"MS",},{"val":(x-40)/20,"s":"HS"}]
    elif 60 < x <= 80: return [{"val":(80-x)/20,"s":"HS",},{"val":(x-60)/20,"s":"VHS"}]
    elif 80 < x <= 100: return [{"val":(100-x)/20,"s":"VHS"}]

def mf_demand(x):
    if 10 <= x <= 25: return [{"val":1+(25-x)/15, "s":"LD"}]
    elif 25 < x <= 50: return [{"val":(50-x)/25, "s":"LD",}, {"val":(x-25)/25, "s":"MD"}]
    elif 50 < x <= 75: return [{"val":(75-x)/25,"s":"MD"}, {"val":(x-50)/25,"s":"HD"}]

def mf_price(x):
    if 0 <= x <=10: return [{"val":(10-x)/10, "s":"VLPG"}]
    elif 10 < x <= 25: return [{"val":(25-x)/15, "s":"VLPG",}, {"val":(x-10)/15, "s":"LPG"}]
    elif 25 < x <= 45: return [{"val":(45-x)/20, "s":"LPG",}, {"val":(x-25)/20, "s":"MPG"}]
    elif 45 < x <= 60: return [{"val":(60-x)/15, "s":"MPG",}, {"val":(x-45)/15, "s":"HPG"}]
    elif 60 < x <= 80: return [{"val":(80-x)/20, "s":"HPG",}, {"val":(x-60)/20, "s":"VHPG"}]
    else: return [{"val":1+x/10, "s":"VHPG"}]
        
def rule(sup, dem):
    if sup == "VLS" and dem == "LD": return "LPG"
    if sup == "VLS" and dem == "MD": return "HPG"
    if sup == "VLS" and dem == "HD": return "VHPG"
    if sup == "LS" and dem == "LD": return "LPG"
    if sup == "LS" and dem == "MD":  return "HPG"
    if sup == "LS" and dem == "HD":  return "VHPG"
    if sup == "MS" and dem == "LD": return "VLPG"
    if sup == "MS" and dem == "MD": return "MPG"
    if sup == "MS" and dem == "HD": return "HPG"
    if sup == "HS" and dem == "LD": return "VLPG"
    if sup == "HS" and dem == "MD": return "MPG"
    if sup == "HS" and dem == "HD": return "MPG"
    if sup == "VHS" and dem == "LD": return "VLPG"
    if sup == "VHS" and dem == "MD": return "LPG"
    if sup == "VHS" and dem == "HD": return "MPG"
    
def defuzzify(sym, val):
    if sym=="VLPG": return (25-(val*15))  
    if sym=="LPG": return (55-(val*5)/2)
    if sym=="MPG": return (85+val*5)/2 
    elif sym=="HPG": return (125-val*5)/2 
    else: return (90-(val*10)) 
    
input_supply = 50
input_demand = 60
fuz_supply = mf_supply(input_supply)
fuz_demand = mf_demand(input_demand)
fuz_price = []
for sup in fuz_supply:
    for dem in fuz_demand:
        sym = rule(sup["s"], dem["s"])
        val = min(sup["val"], dem["val"])
        fuz_price.append({'val': val, "s":sym})
fuz_ans = fuz_price[0]
for data in fuz_price:
    if( data['val'] > fuz_ans['val']):
        fuz_ans = data
print(defuzzify(fuz_ans["s"], fuz_ans["val"]))