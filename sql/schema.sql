CREATE TABLE IF NOT EXISTS "posts" (
    id integer,
    user_id integer,
    title text,
    body text,
    PRIMARY KEY(id)
);