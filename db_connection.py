#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:41:03 2026

@author: evebarr20
"""
import sqlalchemy

def create_connection(filename):
    """
    Create a SQLAlchemy connection to the bank database
    using credentials stored in a vault file.

    Parameters
    ----------
    filename : str
        Path to the vault file.

    Returns
    -------
    engine : sqlalchemy.engine
        Database engine connection.

    """
    # Open file
    with open(filename, "r", encoding = "utf-8") as file:
        # Get username and password
        username = file.readline().strip()
        password = file.readline().strip()
    # Make a connection to the bank database
    engine = sqlalchemy.create_engine(
        f"postgresql://{username}:{password}@localhost:5432/bank"
    )
    # Return the connection
    return engine
