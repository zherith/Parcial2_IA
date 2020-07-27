--
-- PostgreSQL database dump
--

-- Dumped from database version 11.8 (Ubuntu 11.8-1.pgdg18.04+1)
-- Dumped by pg_dump version 11.8 (Ubuntu 11.8-1.pgdg18.04+1)

-- Started on 2020-07-27 18:59:39 -04

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 16397)
-- Name: est; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.est (
    id integer NOT NULL,
    nombre character varying(20),
    paterno character varying(20),
    materno character varying(20)
);


ALTER TABLE public.est OWNER TO postgres;

--
-- TOC entry 2962 (class 0 OID 16397)
-- Dependencies: 196
-- Data for Name: est; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.est (id, nombre, paterno, materno) FROM stdin;
6989411	eduardo	medrano	ayarde
1	jose	huanca	otelo
2	maria	quispe	hurtado
123456	eduarda	medrana	ayarda
85	josefina	huanca	escobar
\.


--
-- TOC entry 2840 (class 2606 OID 16401)
-- Name: est est_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.est
    ADD CONSTRAINT est_pkey PRIMARY KEY (id);


-- Completed on 2020-07-27 18:59:39 -04

--
-- PostgreSQL database dump complete
--

