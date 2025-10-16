from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S23", "+79162345678"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79163456789"),
    Smartphone("Huawei", "P50 Pro", "+79164567890"),
    Smartphone("OnePlus", "11", "+79165678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
        