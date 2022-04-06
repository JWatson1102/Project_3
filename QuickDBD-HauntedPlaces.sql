-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/p5tscX
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "haunted_places" (
    "city" varchar(50)   NOT NULL,
    "country" varchar(50)   NOT NULL,
    "description" varchar   NOT NULL,
    "location" varchar   NOT NULL,
    "state" varchar   NOT NULL,
    "state_abbrev" varchar   NOT NULL,
    "longitude" float   NOT NULL,
    "latitude" float   NOT NULL,
    CONSTRAINT "pk_haunted_places" PRIMARY KEY (
        "city"
     )
);

