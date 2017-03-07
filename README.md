# coolshop-application-assignment
In this README file you will find a set of assignments. The difficulty differs per assignment. If you cannot solve one of the assignment, simply go to the next one.

Please do not hand in the solutions by means of a pull request. Instead, send us the code, for example by uploading it to dropbox or a similar service.

If you have any questions regarding the actual assignments, send us an e-mail.

When asked to implement functions, they are located in the appropriately named files.

## Cardmasks
We want to show payment cards as `CARDTYPE####XXXXXXXX####`, e.g. a VISA card with cardnumber 1234567887654321 becomes `VISA1234XXXXXXXX4321`.
Implement the function to do this:

	get_card_mask(card_type: str, card_number: str) -> str.

## Rounding of Money
We want to show prices as ending in either .50, .95, or .00. We always round *up* to the nearest of these.
Implement the function

    show_pretty_price(value: decimal) -> decimal

As an example, 99.01 becomes 99.50, and 5.50 becomes 5.50, 99.51 becomes 99.95, and 99.96 becomes 100.00.

## Product Feeds
We create feeds with our prices to several price comparison sites, e.g. PriceRunner and Prisjakt.
Some of these sites want XML, others want CSV, and some might want even other formats.
Propose a design to handle the creation of these feeds.
Consider how easy it would be to extend to create other formats.

It is perfectly okay to simply note down your thoughts for this, and not write any code.
If you *do* implement a solution, test it using the product IDs provided in the file `product_feed.py`. Note that any product might at any point in time become unavailable.
Products data can be downloaded from `https://www.coolshop.dk/produkt/{product_id}.json`.

## Premium and Date Handling
We provide a Premium subscription, to let customers buy products cheaper.
The first time a customer signs up for Premium, they get an entire month for free, after that, each month costs 39 DKK.
Payment happens the same day each month, e.g. if a Premium has signed up the 15th, the money will be charged the 15th every month.
To prevent February from causing problems, subscriptions created on the 29th, 30th, and 31st of any month, behave as if they were created on the 1st of the following month instead.
When a Premium subscription is cancelled, the customer is still a Premium member for the rest of the payment period.
If the cancellation happens on the payment day, it is assumed the money has already been charged,

* Implement the function `get_first_payment_date(signup_date: date, previous_premium: boolean) -> date`.
* Implement the function `get_end_date(sign_up_date: date, cancel_date: date) -> date`.
* Implement the function `get_billing_day(signup_date: date) -> int`.

An example could be a new customer signing up for Premium on 2016-07-15. `get_first_payment_date(2016-07-15, False)` would return 2016-08-15 and `get_billing_day` would return 15. If the customer just a day later decides they do not want to be Premium, `get_end_date(2016-07-15, 2016-07-16)` would return 2016-08-15.

Some time later, at 2016-12-29, the customer buys a premium subscription again. This time, `get_first_payment_date(2016-12-29, True)` would return 2017-01-01, and `get_billing_day` would return 1. On 2017-03-01 the customer decides to cancel the Premium subscription again, and `get_end_date(2016-12-29, 2017-03-01)` return 2017-04-01.

## Code Improvements
The function `Ugly_Function` is quite ugly and inefficient, and we want an improved version. Read and understand the function, and implement a more readable and efficient version in `pretty_function`.
