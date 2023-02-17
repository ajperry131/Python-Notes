# The containing folder shows how to create custom packages

from ecommerce.shopping import sales
from ecommerce.shopping.sales import calc_sales, calc_tax
from ecommerce.customer import contact

calc_tax()
calc_sales()

sales.calc_tax()
sales.calc_sales()

contact.contact_customer()

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)