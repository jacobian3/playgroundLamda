# PROGRAM Ex05BottleDeposits:
# READ number of containers of size sm
containers_sm = int(raw_input("Enter the number of small containers:\n"))
# READ number of containers of size lg
containers_lg = int(raw_input("Enter the number of large containers:\n"))
# COMPUTE refund_sm is the number of small containers * 0.10
refund_sm = containers_sm * 0.10
# COMPUTE refund_lr is the number of large containers * 0.25
refund_lr = containers_lg * 0.25
# COMPUTE sum of refunds
sum_of_refunds = refund_sm + refund_lr
# WRITE refund to be received for returning containers in [$ 0.00]
print "refund to be received for all containers is: $%.2f" % sum_of_refunds
# END
