-- script that creates a function SafeDiv that divides (and returns) the first by the second number
-- returns 0 if the second number is equal to 0.

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION IF NOT EXISTS SafeDiv(a INT, b INT)
RETURNS float DETERMINISTIC
BEGIN
        DECLARE result FLOAT DEFAULT 0;

        IF b = 0
        THEN
                RETURN result;
        END IF;
        SET result = a / b;
        RETURN result;
END
$$
DELIMITER ;
