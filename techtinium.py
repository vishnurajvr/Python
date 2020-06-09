from queue import Queue

newyork = [10,20,40,80,160,320]
p_newyork = [120,230,450,774,1400,2820]
newyork_dict = {10:120,20:230,40:450,80:774,160:1400,320:2820}

india = [10,40,80,160,320]
p_india = [140,413,890,1300,2970]
india_dict = {10:140,40:413,80:890,160:1300,320:2970}

china = [10,20,80,160]
p_china = [110,200,670,1180]
china_dict = {10:110,20:200,80:670,160:1180}

options = ['newyork', 'india', 'china']
units_options = {10:'Large',20:'XLarge',40:'2XLarge',80:'4XLarge',160:'8XLarge',320:'10XLarge'}
options_dict = [newyork_dict,india_dict,china_dict]

nq = Queue()    #newyork queue
iq = Queue()    #india queue
cq = Queue()    #china queue

#   This function make a different list 
def probability(city):
    if city == 'newyork':
        li = newyork
    if city == 'india':
        li = india
    if city == 'china':
        li = china
    a = []
    rev = li.copy()
    rev.reverse()
    for x in range(0,len(li)): 
        a.append(li[slice(x,len(li))]) 
        if x == 1: 
            for y in range(1,len(li)): 
                for z in range(1,len(li)): 
                    if (li[slice(y,len(li),z)]) not in a: 
                        a.append(li[slice(y,len(li),z)]) 
    for x in range(0,len(rev)): 
        a.append(rev[slice(x,len(rev))]) 
        if x == 1: 
            for y in range(1,len(rev)): 
                for z in range(1,len(rev)): 
                    if (rev[slice(y,len(rev),z)]) not in a: 
                        a.append(rev[slice(y,len(rev),z)])
    a.sort()
    for x in range(0,len(a)):
        try:
            if a[x] == a[x+1]:
                a.pop(x)
        except:
            pass
    return a

#   How many chance to get to given units
# eg: 1150 units have 320*3 160*1 20*1 30*1 = 1150 like this take more chance
def chance(units,city,li):
    d = {}
    if city == 'newyork':
        q = nq
    if city == 'india':
        q = iq
    if city == 'china':
        q = cq
    for y in li:
        if units != 0:
            d[y] = units//y
            units = units%y
    if units == 0:
        q.put(d.copy())
        d.clear()

#   This one different country and different probability to give chance to 
# store the result in queue
def chance_trigger(units,city,prob):
    for x in prob:
        chance(units=units, city=city,li=x)

#   give to particual city to get item in queue data-structure
def chance_items(city):
    items = []
    if city == 'newyork':
        q = nq
    if city == 'india':
        q = iq
    if city == 'china':
        q = cq
    a = list(q.queue)
    for x in range(0,len(a)):
        y = a[x]
        if y not in items:
            items.append(y)
    return items

#   drop dupllicate and find price details
def cost_detail(city,items):
    e = {}
    price_detail = []
    for item in items:
        value = 0
        for k,v in item.items():
            value += city[k]*v
            e['price'] = value
            pri = "{},{}".format(item,e)
        price_detail.append(pri)
    return price_detail

#   Find minimum price of the total items
# because we want to lower price to achive our goal
def min_price(price_details):
    prices = []
    for x in price_details:
        x = eval(x)
        for y in x:
            for key,value in y.items():
                if key == 'price':
                    prices.append(value)
    return min(prices)

#   Get the details of our achieved min price units details
def result_units(minimum,price):
    for x in price:
        x = eval(x)
        for y in x:
            for key, value in y.items():
                if value == minimum:
                    return x[0]

#   Give to details about minimun priced units
def result_details(city,minimum,res,hr):
    data= []
    for k,v in res.items():
        k = units_options[k]
        if v!=0:
            data.append((k,v))
    output ={}
    output['region'] = city
    output['total_cost'] = f'${minimum*hr}'
    output['machines'] = data
    return output

def main(u,hr):
    datas = []
    json = {}
    for x in range(0,len(options)):
        pro = probability(options[x])
        chance_trigger(u,options[x],prob=pro)
        item = chance_items(options[x])
        cost_details = cost_detail(options_dict[x],items=item)
        min_prices = min_price(cost_details)
        result = result_units(min_prices,cost_details)
        res_units = result_details(options[x],min_prices,result,hr)
        datas.append(res_units.copy())
    json['output'] = datas
    return datas

if __name__ == '__main__':
    data = main(u=1150,hr=1)
    print(data)

# =========================================== your Output ===========================================

output = {
  'Output': [
    {
      'region': 'NewYork',
      'total_cost': '$10150',
      'machines': [
        ('8XLarge',7),
        ('XLarge',1),
        ('Large',1)
      ]
    },
    {
      'region': 'India',
      'total_cost': '$9520',
      'machines': [
        ('8XLarge',7),
        ('Large',3)
      ]
    },
    {
      'region': 'China',
      'total_cost': '$8580',        # this one have $8570 wrong input :(
      'machines': [
        ('8XLarge',7),
        ('XLarge',1),
        ('Large',1)
      ]
    },
  ]
}
# =========================================== My Output ===========================================
#   problem 1) Capacity of 1150 units for 1 Hour
{
  'output': [
    {
      'region': 'newyork',
      'total_cost': '$10150',
      'machines': [
        ('8XLarge',7),
        ('XLarge',1),
        ('Large',1)
      ]
    },
    {
      'region': 'india',
      'total_cost': '$9520',
      'machines': [
        ('8XLarge',7),
        ('Large',3)
      ]
    },
    {
      'region': 'china',
      'total_cost': '$8570',
      'machines': [
        ('8XLarge',7),
        ('XLarge',1),
        ('Large',1)
      ]
    }
  ]
}

#####################################################################################
        #   sample problems are
                        # 230 units for 5 Hours
                        # 100 units for 24 Hours
                        # 1100 units for 12 Hours

#####################################################################################

#   problem 2)  230 units for 5 Hours

# I don't know this answer is correct or wrong!
[
  {
    'region': 'newyork',
    'total_cost': '$11000',
    'machines': [
      ('8XLarge',1),
      ('2XLarge',1),
      ('XLarge',1),
      ('Large',1)
    ]
  },
  {
    'region': 'india',
    'total_cost': '$10665',
    'machines': [
      ('8XLarge',1),
      ('2XLarge',1),
      ('Large',3)
    ]
  },
  {
    'region': 'china',
    'total_cost': '$9450',
    'machines': [
      ('8XLarge',1),
      ('XLarge',3),
      ('Large',1)
    ]
  }
]

#   problem 3)  100 units for 24 Hours
[
  {
    'region': 'newyork',
    'total_cost': '$24096',
    'machines': [
      ('4XLarge',1),
      ('XLarge',1)
    ]
  },
  {
    'region': 'india',
    'total_cost': '$26544',
    'machines': [
      ('2XLarge',2),
      ('Large',2)
    ]
  },
  {
    'region': 'china',
    'total_cost': '$20880',
    'machines': [
      ('4XLarge',1),
      ('XLarge',1)
    ]
  }
]


#   problem 4)  1100 units for 12 Hours
[
  {
    'region': 'newyork',
    'total_cost': '$118248',
    'machines': [
      ('8XLarge',6),
      ('4XLarge',1),
      ('2XLarge',1),
      ('XLarge',1)
    ]
  },
  {
    'region': 'india',
    'total_cost': '$112596',
    'machines': [
      ('8XLarge',6),
      ('4XLarge',1),
      ('2XLarge',1),
      ('Large',2)
    ]
  },
  {
    'region': 'china',
    'total_cost': '$100200',
    'machines': [
      ('8XLarge',6),
      ('4XLarge',1),
      ('XLarge',3)
    ]
  }
]
