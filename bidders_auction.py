bids = {}
bidding_finish = False

def find_highest_bidder(bids_record):
  max_bid = 0
  for record in bids_record:
    if bids_record[record] > max_bid:
      max_bid = bids_record[record]
      winner = record
  return winner
  
while not bidding_finish:
  name = input("Enter name of the bidder: ")
  bid = int(input("Enter bid amount(in Rs): "))
  bids[name] = bid
  
  finish = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if finish == 'no':
    bidding_finish = True

bid_result = find_highest_bidder(bids)
print(f"Winner of the auction is {bid_result}") 