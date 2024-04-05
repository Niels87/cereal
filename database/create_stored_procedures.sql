DROP PROCEDURE IF EXISTS add_item;
--#--new--#
CREATE PROCEDURE add_item (IN
    c_name        VARCHAR(255),
    c_mfr         CHAR,
    c_type        CHAR,
    c_calories    INT,
    c_protein     INT,
    c_fat         INT,
    c_sodium      INT,
    c_fiber       FLOAT,
    c_carbo       FLOAT,
    c_sugars      INT,
    c_potass      INT,
    c_vitamins    INT,
    c_shelf       INT,
    c_weight      FLOAT,
    c_cups        FLOAT,
    c_rating      VARCHAR(255)
    )
Begin
	INSERT INTO cereal (
    name,
    mfr,
    type,
    calories,
    protein,
    fat,
    sodium,
    fiber,
    carbo,
    sugars,
    potass,
    vitamins,
    shelf,
    weight,
    cups,
    rating
    )
	VALUES (
    c_name,
    c_mfr,
    c_type,
    c_calories,
    c_protein,
    c_fat,
    c_sodium,
    c_fiber,
    c_carbo,
    c_sugars,
    c_potass,
    c_vitamins,
    c_shelf,
    c_weight,
    c_cups,
    c_rating
    );
END
--#--new--#
DROP PROCEDURE IF EXISTS get_all;
--#--new--#
CREATE PROCEDURE get_all (OUT result VARCHAR(255))
Begin
	SELECT * FROM cereal;
END
--#--new--#
DROP PROCEDURE IF EXISTS get_by_fieldvalue;
--#--new--#
CREATE PROCEDURE get_by_fieldvalue (IN field VARCHAR(255), IN val VARCHAR(255), OUT result VARCHAR(255))
Begin
	SET @get_by = CONCAT("SELECT * FROM cereal WHERE cereal.", field, "='", val, "'" );
	PREPARE query FROM @get_by;
	EXECUTE query;
	DEALLOCATE PREPARE query;
END