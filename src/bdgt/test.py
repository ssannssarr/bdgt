from storage import (
    save_data,
    load_data
)

data = load_data()
print(data)
data['budget'] = 2000

save_data(data=data)

print(load_data())
