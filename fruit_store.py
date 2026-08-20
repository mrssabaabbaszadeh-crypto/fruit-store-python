""" Fruit Store (2025)
"""

print('*** Welcome to Fruit Store ***')

# ==================== Product Class ====================
class Product:
    def __init__(self, name, price, stock, desc):
        self.name = name
        self.price = price
        self.stock = stock
        self.desc = desc
        
    def reduce_stock(self, quantity):
        if quantity > self.stock:
            print(f'Insufficient stock. Only {self.stock} items available')
            return False
        self.stock -= quantity
        return True

    def __str__(self):
        return f'{self.name}-{self.price} Toman-{self.stock} items'


# ==================== Products ====================
products = {
    101: Product('Red Apple', 23, 65, 'Sweet'),
    102: Product('Melon', 35, 60, 'Sweet'),
    103: Product('Peach', 30, 78, 'Fresh'),
    104: Product('Banana', 35, 65, 'Ripe'),
    105: Product('Orange', 28, 100, 'Vitamin C'),
}

my_cart = {}


# ==================== Display Products ====================
def show_products():
    print('\n' + '-'*62)
    print(f'|{"ID":^6}|{"Name":^15}|{"Price":^10}|{"Stock":^10}|{"Desc":^15}|')
    print('-'*62)

    for code, p in products.items():
        print(f'|{code:^6}|{p.name:^15}|{p.price:^10}|{p.stock:^10}|{p.desc:^15}|')

    print('-'*62)


# ==================== Shopping Cart ====================
def show_my_cart():
    if not my_cart:
        print('Your shopping cart is empty')
        return 0

    print('\n' + '='*50)
    print('Your Shopping Cart:')
    print('='*50)

    total = 0
    for code, item in my_cart.items():
        p = products[code]
        item_total = p.price * item['quantity']
        total += item_total
        print(f"{p.name} | {item['quantity']} x {p.price} = {item_total} Toman")

    print('='*50)
    print(f'Total: {total} Toman')
    print('='*50)
    return total


def add_to_my_cart():
    show_products()

    try:
        code = int(input('Please enter product code: '))

        if code not in products:
            print('Product not found')
            return

        p = products[code]
        quantity = int(input(f'Quantity of {p.name}: '))

        if quantity <= 0:
            print('Quantity must be greater than zero')
            return

        if quantity > p.stock:
            print(f'Only {p.stock} items available')
            return

        if code in my_cart:
            my_cart[code]['quantity'] += quantity
        else:
            my_cart[code] = {'quantity': quantity}

        print(f'{quantity} {p.name}(s) added to cart')

    except:
        print('Please enter a valid number')


def remove_from_my_cart():
    if not my_cart:
        print('Your shopping cart is empty')
        return

    show_my_cart()

    try:
        code = int(input('Enter product code to remove: '))

        if code not in my_cart:
            print('This product is not in your cart')
            return

        p = products[code]
        current = my_cart[code]['quantity']

        quantity = int(input(f'Quantity to remove (max {current}): '))

        if quantity <= 0:
            print('Quantity must be greater than zero')
            return

        if quantity > current:
            print(f'You only have {current} items')
            return

        my_cart[code]['quantity'] -= quantity

        if my_cart[code]['quantity'] == 0:
            del my_cart[code]

        print(f'{quantity} {p.name}(s) removed from cart')

    except:
        print('Please enter a valid number')


def update_my_cart():
    if not my_cart:
        print('Your shopping cart is empty')
        return

    show_my_cart()

    try:
        product_id = int(input('Enter product code to update: '))

        if product_id not in my_cart:
            print('This product is not in your cart')
            return

        product = products[product_id]
        current_qty = my_cart[product_id]['quantity']
        available_stock = product.stock + current_qty

        new_quantity = int(input(f'Enter new quantity (current: {current_qty}, available: {available_stock}): '))

        if new_quantity <= 0: 
            print('Quantity must be greater than zero')
            return

        if new_quantity > available_stock:
            print(f'Only {available_stock} items available')
            return

        my_cart[product_id]['quantity'] = new_quantity
        print(f'{product.name} quantity updated to {new_quantity}')

    except ValueError:
        print('Please enter a valid number')


# ==================== Discount ====================
def apply_discount(total):
    discount = total * 0.1
    new_total = total - discount
    print('\n' + '='*50)
    print('10% discount for all customers!')
    print(f'Original price: {total} Toman')
    print(f'You save: {discount:.0f} Toman')
    print(f'Final price: {new_total:.0f} Toman')
    print('='*50)
    return new_total


# ==================== Invoice & Receipt ====================
def show_invoice():
    if not my_cart:
        print('Shopping cart is empty')
        return None

    print('\n' + '='*50)
    print('Invoice')
    print('='*50)

    total = 0
    for code, item in my_cart.items():
        p = products[code]
        item_total = p.price * item['quantity']
        total += item_total
        print(f"{p.name} x{item['quantity']} = {item_total} Toman")

    print('-'*50)
    print(f'Subtotal: {total} Toman')
    final_total = apply_discount(total)
    print('='*50)
    return final_total


def payment():
    total = show_invoice()
    if total is None:
        return False

    print('\nPayment Methods:')
    print('1. Cash')
    print('2. Bank Card')

    try:
        choice = int(input('Please select 1 or 2: '))

        if choice == 1:
            cash = int(input(f'Amount to pay ({total} Toman): '))
            if cash >= total:
                change = cash - total
                print(f'\nPayment successful! Change: {change} Toman')
                return True
            else:
                print('Insufficient cash')
                return False

        elif choice == 2:
            card = input('Enter last 4 digits of card: ')
            if len(card) == 4 and card.isdigit():
                print('\nPayment successful')
                return True
            else:
                print('Invalid card number')
                return False

        else:
            print('Invalid choice')
            return False

    except:
        print('Payment error')
        return False


def show_receipt():
    if not my_cart:
        print('Shopping cart is empty')
        return

    print('\n' + '='*50)
    print('Payment Receipt')
    print('='*50)

    total = 0
    for code, item in my_cart.items():
        p = products[code]
        item_total = p.price * item['quantity']
        total += item_total
        print(f"{p.name} x{item['quantity']} = {item_total} Toman")

    print('='*50)
    print(f'Amount paid: {total} Toman')
    print('='*50)
    print('Thank you for your purchase!')
    print('Fruit Store')
    print('='*50)


def finalize_purchase():
    if not my_cart:
        print('Shopping cart is empty')
        return

    if payment():
        for code, item in my_cart.items():
            product = products[code]
            product.reduce_stock(item['quantity'])

        show_receipt()
        my_cart.clear()

        print('\nInventory updated')
        show_products()
    else:
        print('Purchase cancelled')


# ==================== Contact Us ====================
def contact_us():
    print('\n' + '='*50)
    print('Contact Us')
    print('='*50)
    print('Phone: +98 21 66061394')
    print('Email: sabastore@fruit.com')
    print('Address: Azadi Street, Tehran')
    print('Hours: 9 AM - 9 PM')
    print('='*50)


# ==================== Help Guide ====================
def help_guide():
    print('\n' + '='*50)
    print('Help Guide')
    print('='*50)
    print('1. Show Products: View all products with codes')
    print('2. Add to Cart: Enter product code and quantity')
    print('3. Remove from Cart: Remove product from cart')
    print('4. View Cart: See your shopping cart')
    print('5. Update Cart: Change product quantity in cart')
    print('6. Show Invoice: View invoice before payment')
    print('7. Payment: Finalize purchase')
    print('8. Contact Us: Get contact information')
    print('9. About Us: Learn about the store')
    print('10. Help: Display this guide')
    print('11. Exit: Leave the store')
    print('='*50)


# ==================== About Us ====================
def about_us():
    print('\n'+'='*50)
    print('About Us')
    print('='*50)
    print('Fruit Store: Serving you since 2021')
    print('Our Vision: Fresh, high-quality fruit at fair prices')
    print('')
    print('Our Story:')
    print('Started as a small shop')
    print('Now we\'ve grown into the city\'s largest fruit store, thanks to you!')
    print('')
    print('Our Values:')
    print('Fresh fruit')
    print('Fair prices')
    print('Fast delivery')
    print('Product guarantee')
    print('98% customer satisfaction')
    print('')
    print('Why choose us?')
    print('Fresh and clean fruit')
    print('Best prices')
    print('Quick support and guidance')
    print('Fruit direct from the orchard')
    print('='*50)


# ==================== Main Menu ====================
while True:
    print('\n' + '='*50)
    print('*** Fruit Store ***')
    print('='*50)
    print('1. Show Products')
    print('2. Add to Cart')
    print('3. Remove from Cart')
    print('4. View Cart')
    print('5. Update Cart')
    print('6. Show Invoice')
    print('7. Payment & Finalize Purchase')
    print('8. Contact Us')
    print('9. About Us')
    print('10. Help')
    print('11. Exit')
    print('='*50)

    choice = input('Please select (1-11): ')

    if choice == '1':
        show_products()
    elif choice == '2':
        add_to_my_cart()
    elif choice == '3':
        remove_from_my_cart()
    elif choice == '4':
        show_my_cart()
    elif choice =='5':
        update_my_cart()
    elif choice == '6':
        show_invoice()
    elif choice == '7':
        finalize_purchase()
    elif choice == '8':
        contact_us()
    elif choice == '9':
        about_us()
    elif choice == '10':
        help_guide()
    elif choice == '11':
        print('\nGoodbye! Visit us again at Fruit Store.')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 11')
