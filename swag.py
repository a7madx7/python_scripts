class Swag():
    def __init__(self, function):
        self.function = function
        
    def __call__(self, *args, **kwargs):
        word = self.function(*args, **kwargs)
        swagged = list(word)
        switch = False
        for i in range(0, len(swagged) - 1):
            if not swagged[i].isdigit():
                switch = not switch 
            if switch:
                swagged[i] = swagged[i].upper()
            else:
                continue
            
                
                
        return "".join(swagged)   

@Swag
def username():
    return 'a7madx7'
                
print(username())
