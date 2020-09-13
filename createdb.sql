create table category(
    codename varchar(255) primary key,
    name varchar(255),
    is_base_action boolean,
    aliases text
);

create table my_action(
   id integer primary key,
   amount integer,
   category_name integer,
   created date,
   raw_text text,
   FOREIGN KEY(category_codename) REFERENCES category(codename)
);

insert into category (codename, name, is_base_action, aliases)
values
    ("sport", "спорт", true, "отжимания, приседания, прыжки")
    ("tea", "чай", true, "чай, кофе")

