<img alt="Eclipse Marketplace" src="https://img.shields.io/eclipse-marketplace/last-update/e.g.%20notepad4e">
There is a Vegetable with the following characteristics:
1. Index
2. Stage of maturity (stages: None, Flowering, Green, Red)

A vegetable 🥔🥕🥒 can:
1. Grow (move to the next stage of maturation)
2. Provide information about your maturity

There is a Tomato with the following characteristics:
1. Index
2. Stage of maturity (stages: None⬜, Flowering, Green🟩, Red🟥)
3. Tomato variety

A tomato 🍅 can: 
1. Grow (move to the next stage of maturation)
2. Provide information about your maturity
3. Provide information about your variety

Since the Tomato is a Vegetable, it inherits all the characteristics of the vegetable and has additional traits.

There is a Tomato Bush 🌱 that:
1. Contains a list of tomatoes that grow on it
2. Contains all varieties of tomato varieties (options: Agatha, De Barao, Oxheart, Cream)

And maybe:
1. Grow with tomatoes
2. Provide information on the maturity of all tomatoes
3. Provide harvest

And there is also a Gardener 👨‍🌾 who has:
1. Name
2. The plant he looks after (bush with tomatoes

And maybe:
1. Take care of the plant
2. Harvest from it

Tests:
1. Call the gardening help ✅
2. Create objects of classes TomatoBush and Gardener ✅
3. Using an object of class Gardener, take care of a bush with tomatoes ✅
4. Try to harvest ✅
5. If the tomatoes are not yet ripe, continue to care for them. ✅
6. Harvest the crop ✅
7. Determine the variety of the harvested crop ✅

//--------------------------------------------------------------- THE CODE ---------------------------------------------------------------\\

class Vegetable:
	__init__  save _index, _state
	grow grow method, which will move the vegetable to the next stage of ripening
	is_ripe  Create an is_ripe () method that will check if the vegetable is ripe (has reached the last stage of ripening)
	_change_state  change status
	_print_state print inforamation about Vegetable

//--------------------------------------------------------------- IN PROGRESS... ---------------------------------------------------------------\\ #02.01.2021
