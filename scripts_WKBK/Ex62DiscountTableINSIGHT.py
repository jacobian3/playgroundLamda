#PROGRAM DiscountTable.Ex62.py3

#SET values 
prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = .60

#FOR price in prices compute and print all prices
for price in prices :
    #COMPUTE 60% discount
    discount_amount = price * discount 
    discount_price = price - discount_amount
    #WRITE original, discount, and new price after disc. 2 decimal precision.
    #?? somehow the '$%5.2f' alligns all of the decimal points; How??
    print("Price: $%5.2f, Discount: $%5.2f, Price with discount: $%5.2f" \
        % (price, discount_amount, discount_price))
#ENDFOR
#END
