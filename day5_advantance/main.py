class Thing(object):


    def __init__(self,name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight

def input_info():
    name_str, price_str, weight_str = input().split()
    return name_str,int(price_str),int(weight_str)

def main():
    max_weight, num_of_thing = map(int,input().split())
    all_things = []
    for _ in range(num_of_thing):
        all_things.append(Thing(*input_info()))
    all_things.sort(key=lambda x:x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f"total take{thing.weight}")
            total_weight += thing.weight
            total_price += thing.price
    print(f"total price is ${total_price}")


if __name__ == "__main__":
    main()
