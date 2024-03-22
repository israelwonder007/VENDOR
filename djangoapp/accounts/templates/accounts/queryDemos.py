# ***(1)Returns all customers from customer table
customers = Customer.objects.all()

# ***(2)Returns first customer in table
firstCustomer = Customer.objects.first()

# ***(3)Returns first customer in table
lastCustomer = Customer.objects.last()

# ***(4)Returns single customer by name
customerByName = Customer.objects.get(name'john Doe')

# ***(5)Returns single customer by name
customerById = Customer.objects.get(id=4)

# ***(6)Returns all orders related to customer (firstCustomer)
firstCustomer.order_set.all()

# ***(7)Returns orders customer name: (Query parent mode)
order = Order.objects.first()
parentName = order.customer.name

# ***(8)Returns products from table with value
products = Product.objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
leastToGreatest = Product.objects.all().order_by('-id')

# ***(10)Returns all products with tag of "Sport": (Query
productsFiltered = Product.objects.filter(tags_name="5")



# Return the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product_name"Ball").count()

# Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders: {'Ball': 2 'BBQ Grill': 1}
        
# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.Charfield(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)  
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.childmodel_set.all()  

# Noticed: "ChildModel" class is in lower case,
#  when you are doing the related set
ex: orders = customer1.order_set.all()
# or
order = order.objects.first()
print(order.customer.name)



