#!/usr/bin/env python3
import psycopg2


def getConnection():
    return psycopg2.connect("host=localhost dbname=nf18_projet user=augustindelaubier password=ramses1a")
