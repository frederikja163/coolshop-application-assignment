# coolshop-application-assignment
In this README file you will find a set of assignments. The difficulty differs per assignment. If you cannot solve one of the assignment, simply go to the next one.

Please do not hand in the solutions by means of a pull request. Instead, send us the code, for example by uploading it to dropbox or a similar service.

If you have any questions regarding the actual assignments, send us an e-mail.

When asked to implement functions, they are located in the appropriately named files.

## A) Cardmasks
We want to show payment cards as `CARDTYPE####XXXXXXXX####`, e.g. a VISA card with cardnumber 1234567887654321 becomes `VISA1234XXXXXXXX4321`.
Implement the function to do this:

	get_card_mask(card_type: str, card_number: str) -> str.

## B) Rounding of Money
We want to show prices as ending in either .50, .95, or .00. We always round *up* to the nearest of these.
Implement the function

    show_pretty_price(value: decimal) -> decimal

As an example, 99.01 becomes 99.50, and 5.50 becomes 5.50, 99.51 becomes 99.95, and 99.96 becomes 100.00.

## C) Product Feeds
We create product feeds with our prices to several price comparison sites, e.g. PriceRunner and Prisjakt.
Some of these sites want XML, some want CSV, and some want even other formats.
Several of these sites only want a subset of our products, e.g., games and consoles, or clothes.

We want a simple way of adding and editing these feeds. Propose a solution that can do the following:

* It must be easy to add a new feed
* When adding a feed, it must be easy to ensure that only products in some categories get added to the feed
* When adding a feed, it must be easy to ensure that products in some categories are *not* added to the feed
* It must be easy to enable and disable feeds
* Each feed should be exactly one format, e.g., CSV or XML. If a receiver wants several formats with the same contents, it should be different feeds
* Adding other supported formats should not be a major task
* When adding a feed, the output format should be chosen among of the supported formats

It is perfectly okay to simply note down your thoughts for this, and not write any code.
If you *do* implement a solution, you can test it using the product IDs provided in the file `product_feed.py`, or find other product IDs from Coolshop. Note that any product might at any point in time become unavailable.
Product data can be downloaded from `https://www.coolshop.dk/api/products/{id}`.

## D) Calculate next delivery day
Customers often like to know when their orders are delivered, so we want to calculate an expected delivery date.

We deliver orders within 1-2 work days in Denmark. If the order is placed before 15:00 (danish time) on a work day the customer can expect the package the following work day. If the order is placed on a non work day or after 15:00 it will be delivered after 2 work days.

We are closed on Danish Public Holidays and in addition do not consider 5th of June (Constitution Day) and 31th of December (New Year’s Eve) as work days.

Write a function that takes a datetime representing the time the order was placed and returns an expected delivery date. Below is some examples of expected behaviour. Notice the use of UTC timezone.

```
>> from datetime import timezone
>> get_delivery_date(datetime.datetime(2021, 5, 20, 12, 51, 32, 199883, tzinfo=timezone.utc))
>> datetime.date(2021, 5, 21)

>> get_delivery_date(datetime.datetime(2021, 5, 20, 13, 3, 31, 245381, tzinfo=timezone.utc))
>> datetime.date(2021, 5, 25)

>> get_delivery_date(datetime.datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc))
>> datetime.date(2020, 12, 30)

>> get_delivery_date(datetime.datetime(2020, 12, 29, 14, 15, 12, 0, tzinfo=timezone.utc))
>> datetime.date(2021, 1, 4)
```

## E) Code Improvements
The function `Ugly_Function` is quite ugly and inefficient, and we want an improved version. Read and understand the function, and implement a more readable and efficient version in `pretty_function`.

## F) Creating Price Intervals for Product Search
A feature of our search system, is that customers can choose intervals of prices, e.g.:

* *-100
* 100-200
* 200-300
* 300-*

If a user selects the `100-200` interval, only the products satisfying `100 <= price < 200` would be part of the search result.

Internally, we call these intervals `buckets`, and the values `to` and `from`. The difference between `to` and `from` we call the `interval`. We want these buckets to be based on the actual prices of our products, and the `interval` on each bucket to be the same, as shown above. It is secondary how many products are be in each bucket.

Implement the function

	create_price_buckets(prices: List[int],
                         multipliers: List[int],
                         min_bucket_count: int,
                         max_bucket_count: int): List[Dict]

* `prices` is a list of prices of all products. For testing, it is fine to use between 1,000 and 1,000,000 values generated by the `random` module. Our prices are generally between 5 and 20,000 DKK. You don't need to consider ører
* `multipliers` is the minimum `interval` size on the buckets. To get a reasonable number of buckets, multiply these values with integers. If `multipliers = [10, 25]`, acceptable values would then be `[10, 25, 20, 50, 30, 75, ...]`
* `min_bucket_count` is the minimum number of buckets we want. A reasonable default value is 3
* `max_bucket_count` is the maximum number of buckets we want. A reasonable default value is 10

Your implementation should satisfy the following reqirements:

* The function returns a list of dictionaries containing the fields `to`, `from`, and `count`, with `count` being the number of products that would be in the bucket
 * It would be very nice, but not required, if `count` is roughly the same value for all buckets
* `min_bucket_count <= actual_bucket_count <= max_bucket_count`
 * If `min_bucket_count > max_bucket_count`, either raise an error, or consider a reasonable way to decide which values to use instead
 * If there are fewer products than `min_bucket_count`, just return a single bucket. Consider what the `to` and `from` values should be
* You will likely need a way to compare two "sets" of buckets, i.e. buckets having different `interval` values. Explain why you chose the one you made


## G) Creating Elasticsearch synonyms file
We use Elasticsearch as our product database, and for powering our search system. Elasticsearch gives the oppotunity for providing a synonym file, consisting of words that are connected and should evaluate to each other during searching. For example, if a user types "ps4" we want to also search for "playstation 4". 

We represent a synonym as a dictionary consisting of two text strings and a synonym type: `{'text1': 'ps4', 'text2': 'playstation 4', 'synonym_type': 'T'}`

where `synonym_type` can be one of the two types:

* One-way, represented by `'O'`: `text1` evaluate to `text2` but not the other way around, e.g., 'Animal' => 'Cat'
* Two-way, represented by `'T'`: Each of the text strings `text1` and `text2` evaluate to the other, e.g., 'wow' <=> 'World Of Warcraft'

Example data are found in `synonyms_data.py`.

We want these synonym dictionaries to be outputted in a text file understandable by Elasticsearch in the following format:

		# Blank lines and lines starting with pound are comments.
		
		# Explicit mappings (one-ways) match any token sequence on the left side of "=>"
		# and replace with all alternatives on the right side.
		i-pod, i pod => ipod,
		sea biscuit, sea biscit => seabiscuit
		
		# Equvivalent synonyms (two-ways) can be listed, seperated by commas.
		# Examples:
		ipod, i-pod, i pod
		wow, world of warcraft
		lol, laughing out loud
		
		# Note that "ipod, i-pod, i pod" is equivalent to the explicit mapping:
		ipod, i-pod, i pod => ipod, i-pod, i pod
	
More information about Elasticsearch synonyms can be found at <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html">Elasticsearch Homepage</a>.

We want the file to contain as few lines as possible., i.e., synonyms should be solved as much as possible. Consider the following:

		{'text1': 'animal', 'text2': 'pet', 'synonym_type': 'T'}
		{'text1': 'pet', 'text2': 'cat', 'synonym_type': 'O'}
		{'text1': 'cat', 'text2': 'garfield', 'synonym_type': 'O'}

Animal and pet points at each other in a two-way relationship. Pet points at cat and cat at garfield. Pet should therefore resolve to cat and garfield. A synonym file for this example is shown below (note that several solutions exists):

		animal, pet => animal, pet, cat, garfield
		cat => cat, garfield

This task can be solved using various strategies. Choose the one you feel statisfying, and describe your thoughts.
		
		
