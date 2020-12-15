CREATE TABLE UFO_Sitings (
	ID FLOAT PRIMARY KEY,
	City VARCHAR,
	State VARCHAR,
	Country VARCHAR,
	Shape VARCHAR,
	Duration VARCHAR,
	Comments VARCHAR,
	Lat FLOAT,
	Long FLOAT,
	Year FLOAT,
	Zipcode FLOAT
);

CREATE TABLE Meteorite_Landings (
	NAME VARCHAR,
	ID FLOAT,
	NameType VARCHAR,
	Class VARCHAR,
	Mass FLOAT,
	Fall VARCHAR,
	Year FLOAT,
	Lat FLOAT,
	Long FLOAT,
	City VARCHAR,
	Zipcode FLOAT,
	State VARCHAR
)