# calling entire package.
# import ecommerce.shipping
#
# ecommerce.shipping.calc_shipping()


# calling from module to specific function
# from ecommerce.shipping import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

# calling entire module
from ecommerce import shipping

shipping.calc_shipping()
shipping.calc_tax()



