### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:


  def checkforAce(self, card): #Indentation error - should be in line with class declaration. checkforAce should be in snake_case
    if card.value = 1: #Should be == operator to check for equality. Indentation should be four spaces compared to def statement above.
      return true
    else
      return false

  dif highest_card(self, card1 card2) #Should say def, not dif. Missing comma between card1 and card2. Variables should be in snake case, e.g. card_1 card_2. Indentation error again.
    if card1.value > card2.value #Should be idented two more spaces in relation to def statement above.
      return card
    else
      return card2
 

 def cards_total(cards):
   total #Total should be set to zero at the start e.g. total = 0
   for card in cards:
     total += card.value
     return "You have a total of" + total #Return statement should be in line with start of for loop, otherwise it's part of the loop with current indentation.


```
