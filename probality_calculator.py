import random
class Hat:
    contents = []
    drawlist = []
    def __init__(self,**kwargs):
        self.contents.clear()
        self.drawlist.clear()
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self,repeat):
        for i in range(repeat):
            number = random.choice(self.contents)
            self.drawlist.append(number)
            self.contents.remove(number)
        return self.drawlist
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    result = []
    wanted_balss = []
    for key,value in expected_balls.items():
        for i in range(value):
            wanted_balss.append(key)
    for i in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        check = all(item in result for item in wanted_balss)
        print(expected_balls)
        if(check):
            count += 1
            hat.contents += hat.drawlist
            hat.drawlist.clear()
            continue
            
        else:
            hat.contents += hat.drawlist
            hat.drawlist.clear()
            continue
    print(count)
    return count / num_experiments

# hat = Hat(red=3, blue=2)
# hat = Hat(red=5, blue=2)
# actual = hat.contents
# print(actual)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, 
    expected_balls={"blue":2,"green":1},
    num_balls_drawn=4, num_experiments=1000)
print(probability)