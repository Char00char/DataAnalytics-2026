/*
a) Answer to first question as full sentence -- Some data included in this the actor Columns are actor_id, first_name, last_name, and last_update
b) Answer to second question as another full sentence -- There is a lot more information offered here. The information includes film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last update 
c) Answer to third question as another full sentence -- The only other table that has actor_id and film_id is the film_actor table
The information on this table would include rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. I would say this information is easy to read, it is structued pretty simple. I can easily follow what is going on and what I could get out of reading this table if I worked at a movie rental store
From the inventory table, you can see inventory_id,	film_id, store_id, last_update
I believe the best tables to do this would be the rental table, the inventory table, and the film table. You would be able to tie the inventory_id between the rental table and the inventory table to confirm which inventory has been rented, and then tie film_id between the inventory table and the film table to get the name of the film. Then tie everything together back with the invertory_id
*/

SELECT rental_date, inventory_id FROM rental;

SELECT inventory_id, film_id FROM inventory;

SELECT film_id, title FROM film;
