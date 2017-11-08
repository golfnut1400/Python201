


def checkout():
    # setup
    total = 0
    count = 0
    moreItems = True



    while moreItems:
        # each item will be tracked for price and number of items
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            # if user did not enter '0' do the following
            count = count + 1
            # track the number of items
            total = total + price
            # add the price of item and adds to total
            print('Subtotal: $', total)
        else:
            moreItems = False
            
            # turns to False when user enters '0'

    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
