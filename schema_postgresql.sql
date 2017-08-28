CREATE TABLE notes ("id" BIGSERIAL PRIMARY KEY,
                    "created" TIMESTAMP DEFAULT now(),
                    "updated" TIMESTAMP DEFAULT now(),
                    "note" VARCHAR(255),
                    "tag" VARCHAR(200));
