--  script that creates a trigger that decreases the quantity of an item after adding a new order.
--  Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

CREATE TRIGGER decrease_item BEFORE INSERT
ON orders FOR EACH Row UPDATE items SET quantity = quantity - NEW.number where name = NEW.item_name;
