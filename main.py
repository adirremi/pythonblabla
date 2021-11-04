
class Dish:
    def __init__(self, name, price, calories, ingredients):
        if price <=0 :
            raise ValueError('No way, we dont give food for free')
        if calories <=0 :
            raise ValueError('No way, there nothing without calories')
        self.name = name
        self.price = price
        self.calories = calories 
        self.ingredients  = ingredients [:]


    def __repr__(self):

       return '%s costs %s NIS and contains: %s\n(only %s calories!)' % (self.name,self.price,self.ingredients,self.calories)
    
       

    def __lt__(self, other):
        return  self.price == other.price and len(self.ingredients) < len(other.ingredients) or self.price < other.price


    def __eq__(self, other):
       return  self.price == other.price and len(self.ingredients) == len(other.ingredients) 
                


    def __le__(self, other):
        return self.price < other.price or  self.price == other.price


    def add_ingredient(self, ingredient, calories):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            self.calories +=calories
        else:
            raise ValueError(ingredient , ' is already a part of the ingredients')

    def remove_ingredient(self, ingredient, calories):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            self.calories -=calories
        else:
            raise ValueError(ingredient , ' is already not a part of the ingredients')


class Beverage:
    def __init__(self, name, price, is_diet):
        if price <=0 :
            raise ValueError('No way, we dont give food for free')
        self.name = name
        self.price = price
        self.is_diet = is_diet
        

    def __repr__(self):
        if self.is_diet:
          return '%s costs %s NIS(diet)' % (self.name,self.price)
        return '%s costs %s NIS' % (self.name,self.price)
        
    



    def get_price(self,size='normal'):
        
        if size not in['normal','big','small'] :
            raise ValueError('Sorry, we dont have this size')
        if size =='normal':
            return self.price
        if size == 'big':
           return self.price*1.2
        if size == 'small':
           return self.price*0.8



class Meal:
    def __init__(self, name, beverage, dishes):
        self.name = name
        self.beverage = beverage
        self.dishes = dishes[:]
        self.price = Meal.get_price(self)
        sumcalories = 0
        for dishes in self.dishes:
            sumcalories +=dishes.calories            
        self.is_diet =  sumcalories <800 and beverage.is_diet
        


    def __repr__(self):
        if self.is_diet:
          return '%s meal costs %s NIS(healthy!)' % (self.name,self.price)
        return '%s meal costs %s NIS' % (self.name,self.price)
        
    


    def get_price(self):      
        price = self.beverage.get_price('small')
        checklist = sorted(self.dishes)
        checker = checklist[0]
        for dish in checklist:
            price+=dish.price
            if checker>dish:
                checker=dish
        
        return price-checker.price
                
    def __contains__(self, ingredient):
      for dish in self.dishes:
        if ingredient in dish.ingredients:
            return True
      return False
         

  
