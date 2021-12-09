Object Oriented Systems CS4773
Assignment 2 
OCT 16 2021

Team Members:
Robert Gonzalez
Audrey Michaud

SOLID GRASP Priciples:
1. Open Closed Pricipal
	All member variables from all classes are private and there are no global varables.
2. Information Expert Pattern
	The responsibility for a deck releted tasks are in the deck class.
3. Creator Pattern
	deck aggregates card objects, so deck is the class that creates instaces of card
4. Protected Variations Pattern
	There is input valedation in wardemo so user error won't affect other stuctures in an unpredictable way. 