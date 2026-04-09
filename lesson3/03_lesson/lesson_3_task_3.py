from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("101000", "Москва", "Тверская", "15", "45")
from_address = Address("197022", "Санкт-Петербург",
                       "Каменноостровский", "10", "12")

# Создаем отправление
mailing = Mailing(to_address, from_address, 350.50, "TRK123456789")

# Печатаем информацию об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")