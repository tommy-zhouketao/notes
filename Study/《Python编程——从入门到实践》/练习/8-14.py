def make_car(brand, model, **properties):
    car = {"brand": brand, "model": model}
    for k, v in properties.items():
        car[k] = v
    return car

car = make_car("sabaru", "outback", color="blue", tow_package=True)
print car
    