CREATE TABLE "public"."content"
(
 "content_id"          serial NOT NULL,
 "speaker_id"          integer NOT NULL,
 "information_id"      integer NOT NULL,
 "addressee_id"        integer NOT NULL,
 "position"            integer NOT NULL,
 "sentiment_score"     float NOT NULL,
 "sentiment_magnitude" float NOT NULL,
 "privacy_score"       float NOT NULL,
 "datetime"            timestamp NOT NULL,
 "text_content"        text NOT NULL,
 "emotion"             text NOT NULL,
 "intent"              text NOT NULL,
 "privacy_indication"  text NOT NULL,
 CONSTRAINT "PK_content" PRIMARY KEY ( "content_id" ),
 CONSTRAINT "FK_content_speaker_person" FOREIGN KEY ( "speaker_id" ) REFERENCES "public"."person" ( "person_id" ),
 CONSTRAINT "FK_content_information_information" FOREIGN KEY ( "information_id" ) REFERENCES "public"."information" ( "information_id" ),
 CONSTRAINT "FK_content_addressee_person" FOREIGN KEY ( "addressee_id" ) REFERENCES "public"."person" ( "person_id" )
);

CREATE INDEX "fkIdx_content_speaker" ON "public"."content"
(
 "speaker_id"
);

CREATE INDEX "fkIdx_content_information" ON "public"."content"
(
 "information_id"
);

CREATE INDEX "fkIdx_content_addressee" ON "public"."content"
(
 "addressee_id"
);



CREATE TABLE "public"."entities"
(
 "entity_id"      serial NOT NULL,
 "content_id"     integer NOT NULL,
 "value"          float NOT NULL,
 "salience_score" float NOT NULL,
 "representation" text NOT NULL,
 "mention_text"   text NOT NULL,
 "type"           text NOT NULL,
 "mention_type"   text NOT NULL,
 "wiki_url"       text NOT NULL,
 "knowledge_mid"  text NOT NULL,
 "currency"       text NOT NULL,
 CONSTRAINT "PK_entities" PRIMARY KEY ( "entity_id" ),
 CONSTRAINT "FK_entities_content_content" FOREIGN KEY ( "content_id" ) REFERENCES "public"."content" ( "content_id" )
);

CREATE INDEX "fkIdx_entities_content" ON "public"."entities"
(
 "content_id"
);



CREATE TABLE "public"."information"
(
 "information_id"      serial NOT NULL,
 "sentiment_score"     float NOT NULL,
 "sentiment_magnitude" float NOT NULL,
 "datetime"            timestamp NOT NULL,
 "eavesdropping"       boolean NOT NULL,
 "topics"              text[] NOT NULL,
 CONSTRAINT "PK_information" PRIMARY KEY ( "information_id" )
);



CREATE TABLE "public"."person"
(
 "person_id" serial NOT NULL,
 "aliases"   text[] NOT NULL,
 CONSTRAINT "PK_person" PRIMARY KEY ( "person_id" )
);



CREATE TABLE "public"."person_information"
(
 "pi_id"          serial NOT NULL,
 "person_id"      integer NOT NULL,
 "information_id" integer NOT NULL,
 CONSTRAINT "PK_pi" PRIMARY KEY ( "pi_id" ),
 CONSTRAINT "FK_pi_person_person" FOREIGN KEY ( "person_id" ) REFERENCES "public"."person" ( "person_id" ),
 CONSTRAINT "FK_pi_information_information" FOREIGN KEY ( "information_id" ) REFERENCES "public"."information" ( "information_id" )
);

CREATE INDEX "fkIdx_pi_person" ON "public"."person_information"
(
 "person_id"
);

CREATE INDEX "fkIdx_pi_information" ON "public"."person_information"
(
 "information_id"
);



CREATE TABLE "public"."person_trust"
(
 "pt_id"      serial NOT NULL,
 "truster_id" integer NOT NULL,
 "trustee_id" integer NOT NULL,
 "trust"      float NOT NULL,
 CONSTRAINT "PK_person_trust" PRIMARY KEY ( "pt_id" ),
 CONSTRAINT "FK_pt_truster_person" FOREIGN KEY ( "truster_id" ) REFERENCES "public"."person" ( "person_id" ),
 CONSTRAINT "FK_pt_trustee_person" FOREIGN KEY ( "trustee_id" ) REFERENCES "public"."person" ( "person_id" )
);

CREATE INDEX "fkIdx_pt_truster" ON "public"."person_trust"
(
 "truster_id"
);

CREATE INDEX "fkIdx_pt_trustee" ON "public"."person_trust"
(
 "trustee_id"
);



CREATE TABLE "public"."person_content"
(
 "pc_id"          serial NOT NULL,
 "person_id"      integer NOT NULL,
 "content_id"     integer NOT NULL,
 "control_level"  text NOT NULL,
 CONSTRAINT "PK_pc" PRIMARY KEY ( "pc_id" ),
 CONSTRAINT "FK_pc_person_person" FOREIGN KEY ( "person_id" ) REFERENCES "public"."person" ( "person_id" ),
 CONSTRAINT "FK_pc_content_content" FOREIGN KEY ( "content_id" ) REFERENCES "public"."content" ( "content_id" )
);

CREATE INDEX "fkIdx_pc_person" ON "public"."person_content"
(
 "person_id"
);

CREATE INDEX "fkIdx_pc_information" ON "public"."person_content"
(
 "content_id"
);
